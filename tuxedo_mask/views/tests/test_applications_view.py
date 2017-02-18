# -*- coding: utf-8 -*-

from nose.tools import assert_true

from . import BaseTestCase
from tuxedo_mask import models, views


class TestApplicationsView(BaseTestCase):

    @property
    def _Model(self):
        return models.Applications

    @property
    def _View(self):
        return views.ApplicationsView

    @property
    def fields(self):
        return ['applications_sid', 'name']

    @property
    def values(self):
        return ['foo', 'foo']

    def set_up_serialization_fails_silently(self):
        pass

    def test_name_maximum_length(self):
        data = dict(zip(self.fields, self.values))
        data['name'] = 'x' * 50
        self.data = data

        self.unmarshall()

        assert_true(self.unmarshalled_result.errors)

