# -*- coding: utf-8 -*-

import flask
import flask_restful

from . import authentication
from tuxedo_mask import views


class LoginAttemptsResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        # TODO (duyn): Log user login attempt.

        login_attempt = (
            views.LoginAttemptsView().load(data=flask.request.get_json()).data)

        application = flask.g.service.applications.get_by_sid(applications_sid)
        is_authenticated = flask.g.service.verify_credentials(
            header=login_attempt['credentials'],
            scope=application)

        flask.g.body = {'is_authenticated': is_authenticated}

        return flask.g.get_response()

