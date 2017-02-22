#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import logging

import flask
import flask_restful

from tuxedo_mask import resources, services

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

api.add_resource(resources.ApplicationsCollectionResource, '/v1/applications/')
api.add_resource(resources.UsersCollectionResource, '/v1/applications/<string:applications_sid>/users/')


@app.before_request
def do_before_request():
    flask.g.logger = logging.getLogger(name='tuxedo_mask')
    flask.g.service = services.TuxedoMaskService.from_configuration()

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

