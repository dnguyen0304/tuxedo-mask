# -*- coding: utf-8 -*-

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
        return ['name']

    @property
    def values(self):
        return ['foo']

    def test_deserialization_name_minimum_length(self):
        self.help_validate(field='name', value='', keyword='length')

    def test_deserialization_name_maximum_length(self):
        self.help_validate(field='name', value='x' * 50, keyword='length')

