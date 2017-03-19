# -*- coding: utf-8 -*-

import flask
import flask_restful

from . import authentication
from tuxedomask import views


class LoginAttemptsResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        flask.g.message.update({'topic': 'LoginAttempt', 'state': 'Pending'})
        flask.g.logger.info('', extra=flask.g.message)

        login_attempt = (
            views.LoginAttemptsView().load(data=flask.request.get_json()).data)

        flask.g.message.update({
            'state': 'Starting',
            'encoded_credentials': flask.request.get_json()['credentials']})
        flask.g.logger.info('', extra=flask.g.message)

        application = flask.g.service.applications.get_by_sid(applications_sid)
        is_authenticated = flask.g.service.verify_credentials(
            header=login_attempt['credentials'],
            scope=application)

        flask.g.body = {'is_authenticated': is_authenticated}

        flask.g.message.update({'state': 'Complete'})
        flask.g.logger.info('', extra=flask.g.message)

        return flask.g.get_response()

