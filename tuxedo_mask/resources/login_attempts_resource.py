# -*- coding: utf-8 -*-

import flask
import flask_restful

from . import authentication
from tuxedo_mask import views


class LoginAttemptsResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        flask.g.event.update({'event_name': 'LoginAttemptEvent',
                              'event_state': 'PENDING'})
        flask.g.logger.info('', extra=flask.g.event)

        login_attempt = (
            views.LoginAttemptsView().load(data=flask.request.get_json()).data)

        flask.g.event.update({
            'event_state': 'STARTING',
            'encoded_credentials': flask.request.get_json()['credentials']})
        flask.g.logger.info('', extra=flask.g.event)

        application = flask.g.service.applications.get_by_sid(applications_sid)
        is_authenticated = flask.g.service.verify_credentials(
            header=login_attempt['credentials'],
            scope=application)

        flask.g.body = {'is_authenticated': is_authenticated}

        flask.g.event.update({'event_state': 'COMPLETE'})
        flask.g.logger.info('', extra=flask.g.event)

        return flask.g.get_response()

