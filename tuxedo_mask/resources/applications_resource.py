# -*- coding: utf-8 -*-

import collections
import http
import logging

import flask
import flask_restful
import marshmallow

from tuxedo_mask import repositories, services, views


class ApplicationsCollectionResource(flask_restful.Resource):

    def __init__(self):
        # Flask-RESTful constructs a new Resource for every request.
        # Should these be global objects?
        self.logger = logging.getLogger('tuxedo_mask')
        self.service = services.TuxedoMaskService.from_configuration()

    # Although initially counter-intuitive, Tuxedo Mask actually
    # delegates to itself for authentication. How this works is the
    # service automatically registers itself as an Application. This
    # occurs when it is first provisioned, i.e. at build-time. Clients
    # are then Users of this reserved Application.
    #
    # In summary, while POST requests are made to the Applications
    # Resource, Applications must also be added to the repository as
    # Users.
    def post(self):
        # TODO (duyn): Log application registration / sign-up.

        body = collections.OrderedDict()
        http_status_code = None
        headers = dict()

        applications_view = views.ApplicationsView()
        users_view = views.UsersView()
        users_view.fields['username'].load_from = 'name'
        data = flask.request.get_json()

        try:
            application = applications_view.load(data=data).data
            user = users_view.load(data=data).data
        except marshmallow.exceptions.ValidationError as e:
            http_status_code = http.HTTPStatus.BAD_REQUEST
            self.logger.info(e.messages)
            return body, http_status_code, headers

        tuxedo_mask_application = self.service.applications.get_by_name(
            name='tuxedo_mask')
        user.applications_id = tuxedo_mask_application.applications_id
        self.service.applications.add(entity=application, by=tuxedo_mask_application)
        self.service.users.add(entity=user, by=tuxedo_mask_application)

        try:
            self.service.commit()
        except repositories.EntityConflict:
            http_status_code = http.HTTPStatus.CONFLICT
            message = ("""There is already an existing application with the """
                       """name "{name}".""")
            self.logger.info(message.format(name=application.name))
        else:
            http_status_code = http.HTTPStatus.CREATED
            # TODO (duyn): Log resource creation.

        self.service.dispose()

        return body, http_status_code, headers

