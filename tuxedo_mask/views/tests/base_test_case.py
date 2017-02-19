# -*- coding: utf-8 -*-

import abc
import inspect
import sys

import marshmallow
import nose
from nose.tools import assert_false


class BaseTestCase(metaclass=abc.ABCMeta):

    def __init__(self):
        self.data = dict()
        self.marshalled_result = None
        self.unmarshalled_result = None

    @property
    @abc.abstractmethod
    def _Model(self):
        pass

    @property
    @abc.abstractmethod
    def _View(self):
        pass

    @property
    @abc.abstractmethod
    def fields(self):
        pass

    @property
    @abc.abstractmethod
    def values(self):
        pass

    def setup(self):
        self.data = dict(zip(self.fields, self.values))
        self._help_marshall()
        self._help_unmarshall()

    def _help_marshall(self):
        arguments = self._match_call_signature(callable_=self._Model,
                                               arguments=self.data)
        entity = self._Model(**arguments)
        self.marshalled_result = self._View().dump(obj=entity)

    def unmarshall_with(self, update):

        """
        Unmarshall (i.e. "load") the data into an object.

        Parameters
        ----------
        update : dict
            New values with which to update the already initialized
            data.
        """

        data_ = dict(zip(self.fields, self.values))
        data_.update(update)
        self.data = data_
        self._help_unmarshall()

    def _help_unmarshall(self):
        self.unmarshalled_result = self._View().load(data=self.data)

    @staticmethod
    def _match_call_signature(callable_, arguments):
        parameters = inspect.signature(callable_).parameters
        if 'kwargs' not in parameters:
            arguments = {parameter_name: arguments[parameter_name]
                         for parameter_name
                         in parameters}
        return arguments

    def test_serialization_has_no_errors(self):
        assert_false(self.marshalled_result.errors)

    @abc.abstractmethod
    def set_up_serialization_fails_silently(self):
        pass

    def test_serialization_fails_silently(self):
        self.set_up_serialization_fails_silently()

        test_case_name = sys._getframe(0).f_code.co_name
        e = marshmallow.exceptions.ValidationError

        try:
            self._help_marshall()
        except e:
            # The recommended way to assert that a test case does not
            # raise a specific error or exception is to use
            # unittest.TestCase.fail(). The technique here reflects its
            # implementation.
            message = '{test_case_name}() should not raise {e_name}.'
            raise AssertionError(message.format(test_case_name=test_case_name,
                                                e_name=e.__name__))

    def test_deserialization_has_no_errors(self):
        assert_false(self.unmarshalled_result.errors)

    @staticmethod
    def test_configured_datetime_format():
        raise nose.SkipTest

    @staticmethod
    def test_configured_read_only_fields():
        raise nose.SkipTest

    @staticmethod
    def test_configured_required_fields():
        raise nose.SkipTest

    @staticmethod
    def test_configured_sort_order():
        raise nose.SkipTest

