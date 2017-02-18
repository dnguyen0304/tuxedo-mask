# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields, validate

from . import BaseView
from tuxedo_mask import models


class _ApplicationsView(marshmallow.Schema):

    name_error_message = ("""The application name must be between {min} """
                          """and {max} characters in length.""")

    applications_sid = fields.String(dump_only=True)
    name = fields.String(
        required=True,
        validate=[validate.Length(min=1, max=32, error=name_error_message)])


# If ApplicationsView subclassed BaseView directly, the metadata fields
# in the parent would be sorted above the domain fields in the child.
# This defeats the purpose of applying that characteristic through the
# Meta paradigm.
class ApplicationsView(BaseView, _ApplicationsView):

    _Model = models.Applications

