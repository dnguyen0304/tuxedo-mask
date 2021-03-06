# -*- coding: utf-8 -*-

import abc
import inspect
import sys

import marshmallow
import nose
from nose.tools import assert_false, assert_in


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

        # Marshall.
        arguments = self._match_call_signature(callable_=self._Model,
                                               arguments=self.data)
        entity = self._Model(**arguments)
        self.marshalled_result = self._View().dump(obj=entity)

        # Unmarshall.
        self.unmarshalled_result = self._View().load(data=self.data)

    @staticmethod
    def _match_call_signature(callable_, arguments):
        parameters = inspect.signature(callable_).parameters
        if 'kwargs' not in parameters:
            arguments = {parameter_name: arguments[parameter_name]
                         for parameter_name
                         in parameters}
        return arguments

    def help_validate(self, field, value, keyword):

        """
        Run a test to assert validation was configured correctly.

        The validation configuration must include specifying a helpful
        error message.

        Parameters
        ----------
        field : str
            Field name to validate.
        value : Any
            Field value to validate.
        keyword : str
            Keyword to search within the error message for.

        Raises
        ------
        AssertionError
            If validation was not configured correctly.
        """

        try:
            self._View().validate(data={field: value}, partial=True)
        except marshmallow.exceptions.ValidationError as e:
            assert_in(field, e.messages)
            assert_in(keyword, e.messages[field][0])
        else:
            test_name = sys._getframe(2).f_code.co_name

            # The recommended way is to assert a test does not raise a
            # specific error or exception is to use
            # unittest.TestCase.fail(). The technique here reflects its
            # implementation.
            message = ("""{test_name}() should raise """
                       """marshmallow.exceptions.ValidationError.""")
            raise AssertionError(message.format(test_name=test_name))

    def test_serialization_has_no_errors(self):
        assert_false(self.marshalled_result.errors)

    def test_deserialization_has_no_errors(self):
        assert_false(self.unmarshalled_result.errors)

    @staticmethod
    def test_configured_read_only_fields():
        raise nose.SkipTest

    @staticmethod
    def test_configured_required_fields():
        raise nose.SkipTest

    @staticmethod
    def test_configured_write_only_fields():
        raise nose.SkipTest

