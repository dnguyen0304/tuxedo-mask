# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields


class LoginAttemptsView(marshmallow.Schema):

    class Meta:
        strict = True

    credentials = fields.String(required=True)

    @marshmallow.post_load
    def prepend_authentication_scheme(self, data):
        data_ = data.copy()
        try:
            data_['credentials'] = 'Basic ' + data_['credentials']
        except KeyError:
            pass
        return data_

