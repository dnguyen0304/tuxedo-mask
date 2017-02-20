# -*- coding: utf-8 -*-

from nose.tools import assert_in

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
        self.unmarshall_with(update={'name': ''})

    def test_deserialization_name_minimum_length(self):
        errors = self._View().validate(data={'name': ''}, partial=True)
        assert_in('name', errors)

    def test_deserialization_name_maximum_length(self):
        errors = self._View().validate(data={'name': 'x' * 50}, partial=True)
        assert_in('name', errors)

