# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields

from tuxedo_mask import models


class BaseView(marshmallow.Schema):

    _model = models.Base

    class Meta:
        dateformat = 'iso'
        ordered = True

    created_at = fields.DateTime(dump_only=True)
    created_by = fields.String(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    updated_by = fields.String(dump_only=True)

    @marshmallow.post_load
    def _deserialize(self, data):
        return self._model(**data)

