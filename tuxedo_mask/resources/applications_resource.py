# -*- coding: utf-8 -*-

import http

import flask
import flask_restful

from tuxedo_mask import views


class ApplicationsCollectionResource(flask_restful.Resource):

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

        users_view = views.UsersView()
        users_view.fields['username'].load_from = 'name'

        application = views.ApplicationsView().load(data=flask.request.get_json()).data
        user = users_view.load(data=flask.request.get_json()).data

        tuxedo_mask_application = flask.g.service.applications.get_by_name(
            name='tuxedo_mask')
        user.applications_id = tuxedo_mask_application.applications_id
        flask.g.service.applications.add(entity=application, by=tuxedo_mask_application)
        flask.g.service.users.add(entity=user, by=tuxedo_mask_application)
        flask.g.service.commit()

        flask.g.http_status_code = http.HTTPStatus.CREATED
        # TODO (duyn): Log resource creation.

        return flask.g.get_response()

