# -*- coding: utf-8 -*-

import http

import flask
import flask_restful

from . import authentication
from tuxedomask import views


class UsersCollectionResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        flask.g.message.update({'topic': 'UserAdd', 'state': 'Pending'})
        flask.g.logger.info('', extra=flask.g.message)

        user = views.UsersView().load(data=flask.request.get_json()).data

        flask.g.message.update({
            'state': 'Starting',
            'application_sid': applications_sid,
            'user_username': user.username,
            'user_encoded_password': flask.request.get_json()['password']})
        flask.g.logger.info('', extra=flask.g.message)

        application = flask.g.service.applications.get_by_sid(applications_sid)
        user.applications_id = application.applications_id
        flask.g.service.users.add(entity=user, by=application)
        flask.g.service.commit()

        flask.g.http_status_code = http.HTTPStatus.CREATED

        flask.g.message.update({'state': 'Complete'})
        flask.g.logger.info('', extra=flask.g.message)

        return flask.g.get_response()

