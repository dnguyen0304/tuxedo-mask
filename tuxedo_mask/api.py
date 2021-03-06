#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import http
import logging
import sys
import traceback
import uuid

import flask
import flask_restful
import marshmallow

from tuxedo_mask import repositories, services, resources

app = flask.Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = flask_restful.Api(app=app)

api.add_resource(resources.ApplicationsCollectionResource, '/v1/applications/')
api.add_resource(resources.ApplicationsResource, '/v1/applications/<string:applications_sid>')
api.add_resource(resources.LoginAttemptsResource, '/v1/applications/<string:applications_sid>/login_attempts/')
api.add_resource(resources.UsersCollectionResource, '/v1/applications/<string:applications_sid>/users/')


@app.before_request
def do_before_request():

    # Flask-RESTful constructs a new Resource on every request. Should
    # these be global objects?
    flask.g.logger = logging.getLogger(name='tuxedomask')
    flask.g.service = services.TuxedoMaskService.from_configuration()

    flask.g.message = {'topic': '', 'requests_uuid': str(uuid.uuid4())}
    flask.g.body = collections.OrderedDict()
    flask.g.http_status_code = None
    flask.g.headers = dict()

    def get_response():
        return flask.g.body, flask.g.http_status_code, flask.g.headers

    flask.g.get_response = get_response

    extra = {'topic': 'ConnectionPooling'}
    extra.update({'requests_uuid': flask.g.message['requests_uuid']})
    extra.update(services.TuxedoMaskService.get_connection_pool_status())
    flask.g.logger.info('', extra=extra)


@app.after_request
def do_after_request(response):

    flask.g.service.dispose()

    extra = {'topic': 'ConnectionPooling'}
    extra.update({'requests_uuid': flask.g.message['requests_uuid']})
    extra.update(services.TuxedoMaskService.get_connection_pool_status())
    flask.g.logger.info('', extra=extra)

    return response


@app.errorhandler(Exception)
def handle_exception(e):

    message = ''.join(traceback.format_exception_only(*sys.exc_info()[:2]))
    response = flask.jsonify(dict())
    response.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
    log_e(message=message, e=e, is_internal_e=True)

    return response


@app.errorhandler(repositories.EntityConflict)
def handle_entity_conflict(e):

    message_mapping = {
        'applicationscollectionresource': (
            """There is already an existing application with this name."""),
        'userscollectionresource': (
            """There is already an existing user with this username.""")}

    message = message_mapping[flask.request.endpoint]
    response = flask.jsonify(message)
    response.status_code = http.HTTPStatus.CONFLICT
    log_e(message=message, e=e)

    return response


@app.errorhandler(marshmallow.exceptions.ValidationError)
def handle_validation_error(e):

    response = flask.jsonify(e.messages)
    response.status_code = http.HTTPStatus.BAD_REQUEST
    log_e(message='There was an error when trying to validate the data.', e=e)

    return response


def log_e(message, e, is_internal_e=False):

    extra = flask.g.message.copy()
    extra.update(dict([
        ('error_type', '.'.join([e.__class__.__module__, e.__class__.__name__])),
        ('error_message', str(e)),
        ('users_sid', ''),
        ('user_username', ''),
        ('request_client_ip_address', flask.request.environ.get('REMOTE_ADDR')),
        ('request_client_port_number', flask.request.environ.get('REMOTE_PORT')),
        ('request_method', flask.request.environ.get('REQUEST_METHOD')),
        ('request_url', flask.request.url),
        ('request_authorization', flask.request.environ.get('HTTP_AUTHORIZATION')),
        ('request_body', flask.request.get_data().decode('utf-8')),
        ('request_host', flask.request.host),
        ('request_endpoint_name', flask.request.endpoint)]))
    extra.update({'state': 'Complete'})

    try:
        extra['users_sid'] = flask.g.user.users_sid
        extra['user_username'] = flask.g.user.username
    except AttributeError:
        pass

    if is_internal_e:
        flask.g.logger.exception(message, extra=extra)
    else:
        flask.g.logger.error(message, extra=extra)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

