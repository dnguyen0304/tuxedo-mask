# -*- coding: utf-8 -*-

import datetime

from nose.tools import assert_equal, assert_true

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

    def test_configured_iso_datetime_format(self):
        assert_equal(self._View.Meta.dateformat, 'iso')

    def test_configured_maintaining_sort_order(self):
        assert_true(self._View.Meta.ordered)

    def test_configured_raising_validation_errors(self):
        assert_true(self._View.Meta.strict)

