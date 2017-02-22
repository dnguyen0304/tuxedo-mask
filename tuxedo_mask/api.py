#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import flask_restful

from tuxedo_mask import resources

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

api.add_resource(resources.ApplicationsCollectionResource, '/v1/applications/')
api.add_resource(resources.UsersCollectionResource, '/v1/applications/<string:users_sid>/users/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

