# -*- coding: utf-8 -*-

import datetime

from . import BaseTestCase
from tuxedo_mask import models, views


class TestBaseView(BaseTestCase):

    @property
    def _Model(self):
        return models.Base

    @property
    def _View(self):
        return views.BaseView

    @property
    def fields(self):
        return ['created_at', 'created_by', 'updated_at', 'updated_by']

    @property
    def values(self):
        return [datetime.datetime.now(tz=datetime.timezone.utc), '-1'] * 2

    def set_up_serialization_fails_silently(self):
        self.unmarshall_with(update={'created_at': 'foo'})

