# -*- coding: utf-8 -*-

import collections
import logging

import flask_restful

from . import authentication
from tuxedo_mask import services


class UsersCollectionResource(flask_restful.Resource):

    def __init__(self):
        self.logger = logging.getLogger('tuxedo_mask')
        self.service = services.TuxedoMaskService.from_configuration()

    @authentication.login_required
    def post(self, users_sid):

        body = collections.OrderedDict()
        http_status_code = None
        headers = dict()

        return body, http_status_code, headers

