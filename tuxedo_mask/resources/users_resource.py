# -*- coding: utf-8 -*-

import http

import flask
import flask_restful

from . import authentication
from tuxedo_mask import views


class UsersCollectionResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        flask.g.event.update({'event_name': 'UserAdd',
                              'event_state': 'PENDING'})
        flask.g.logger.info('', extra=flask.g.event)

        user = views.UsersView().load(data=flask.request.get_json()).data

        flask.g.event.update({
            'event_state': 'STARTING',
            'application_sid': applications_sid,
            'user_username': user.username,
            'user_encoded_password': flask.request.get_json()['password']})
        flask.g.logger.info('', extra=flask.g.event)

        application = flask.g.service.applications.get_by_sid(applications_sid)
        user.applications_id = application.applications_id
        flask.g.service.users.add(entity=user, by=application)
        flask.g.service.commit()

        flask.g.http_status_code = http.HTTPStatus.CREATED

        flask.g.event.update({'event_state': 'COMPLETE'})
        flask.g.logger.info('', extra=flask.g.event)

        return flask.g.get_response()

