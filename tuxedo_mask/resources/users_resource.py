# -*- coding: utf-8 -*-

import http

import flask
import flask_restful
import marshmallow

from . import authentication
from tuxedo_mask import repositories, views


class UsersCollectionResource(flask_restful.Resource):

    @authentication.login_required
    def post(self, applications_sid):
        # TODO (duyn): Log user creation.

        try:
            user = views.UsersView().load(data=flask.request.get_json()).data
        except marshmallow.exceptions.ValidationError as e:
            flask.g.http_status_code = http.HTTPStatus.BAD_REQUEST
            flask.g.logger.info(e.messages)
            return flask.g.get_response()

        application = flask.g.service.applications.get_by_sid(applications_sid)
        user.applications_id = application.applications_id
        flask.g.service.users.add(entity=user, by=application)

        try:
            flask.g.service.commit()
        except repositories.EntityConflict:
            flask.g.http_status_code = http.HTTPStatus.CONFLICT
            message = ("""There is already an existing user with the """
                       """username "{username}".""")
            flask.g.logger.info(message.format(username=user.username))
        else:
            flask.g.http_status_code = http.HTTPStatus.CREATED
            # TODO (duyn): Log resource creation.

        return flask.g.get_response()

