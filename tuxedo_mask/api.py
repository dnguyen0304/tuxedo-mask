#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import http
import logging
import uuid

import flask
import flask_restful
import marshmallow

from tuxedo_mask import repositories, services, resources

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

api.add_resource(resources.ApplicationsCollectionResource, '/v1/applications/')
api.add_resource(resources.UsersCollectionResource, '/v1/applications/<string:applications_sid>/users/')


@app.before_request
def do_before_request():

    flask.g.logger = logging.getLogger(name='tuxedo_mask')
    flask.g.service = services.TuxedoMaskService.from_configuration()

    flask.g.requests_id = str(uuid.uuid4())
    flask.g.body = collections.OrderedDict()
    flask.g.http_status_code = None
    flask.g.headers = dict()

    def get_response():
        return flask.g.body, flask.g.http_status_code, flask.g.headers

    flask.g.get_response = get_response


@app.after_request
def do_after_request(response):

    flask.g.service.dispose()

    return response


@app.errorhandler(repositories.EntityConflict)
def handle_entity_conflict(e):

    message = 'There is already an existing user with this username.'
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


def log_e(message, e):

    extra = dict([
        ('e_type', '.'.join([e.__class__.__module__, e.__class__.__name__])),
        ('e_message', str(e)),
        ('requests_id', flask.g.requests_id),
        ('users_sid', flask.g.user.users_sid),
        ('user_username', flask.g.user.username),
        ('request_client_ip_address', flask.request.environ.get('REMOTE_ADDR')),
        ('request_client_port_number', flask.request.environ.get('REMOTE_PORT')),
        ('request_method', flask.request.environ.get('REQUEST_METHOD')),
        ('request_url', flask.request.url),
        ('request_authorization', flask.request.environ.get('HTTP_AUTHORIZATION')),
        ('request_body', flask.request.get_data().decode('utf-8')),
        ('request_host', flask.request.host),
        ('request_endpoint_name', flask.request.endpoint)])

    flask.g.logger.error(message, extra=extra)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

