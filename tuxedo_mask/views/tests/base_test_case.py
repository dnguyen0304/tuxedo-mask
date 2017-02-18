# -*- coding: utf-8 -*-

import datetime
import sys

import marshmallow
import nose
from nose.tools import assert_equal, assert_false, assert_true

from tuxedo_mask import models, views


class BaseTestCase:

    def __init__(self):
        self.fields = ['created_at', 'created_by', 'updated_at', 'updated_by']
        self.values = [datetime.datetime.now(tz=datetime.timezone.utc),
                       '-1',
                       datetime.datetime.now(tz=datetime.timezone.utc),
                       '-1']

        self.data = dict()
        self.entity = None
        self.marshalled_result = None
        self.unmarshalled_result = None

    def setup(self):
        self.data = dict(zip(self.fields, self.values))
        self.entity = models.Base(**self.data)
        self.marshalled_result = views.BaseView().dump(obj=self.entity)
        self.unmarshalled_result = views.BaseView().load(data=self.data)

    def test_serialization_has_no_errors(self):
        assert_false(self.marshalled_result.errors)

    def test_serialization_fails_silently(self):
        test_case_name = sys._getframe(0).f_code.co_name
        e = marshmallow.exceptions.ValidationError

        self.values[self.fields.index('created_at')] = 'foo'

        try:
            self.setup()
        except e:
            # The recommended way to assert that a test case does not
            # raise a specific error or exception is to use
            # unittest.TestCase.fail(). The technique here reflects its
            # implementation.
            message = '{test_case_name}() should not raise {e_name}.'
            raise AssertionError(message.format(test_case_name=test_case_name,
                                                e_name=e.__name__))

    def test_serialization_maintains_sort_order(self):
        data = self.marshalled_result.data
        for key, field in zip(data, self.fields):
            assert_equal(key, field)

    @staticmethod
    def test_serialization_uses_iso_datetime_format():
        raise nose.SkipTest

    def test_deserialization_has_no_errors(self):
        assert_false(self.unmarshalled_result.errors)

    def test_deserialization_enforces_read_only_fields(self):
        base = self.unmarshalled_result.data
        for field, value in zip(self.fields, self.values):
            assert_true(getattr(base, field) != value)

