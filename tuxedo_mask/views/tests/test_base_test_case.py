# -*- coding: utf-8 -*-

from nose.tools import assert_dict_equal

from . import BaseTestCase


class TestBaseTestCase:

    class FooModel:
        def __init__(self, foo):
            pass

    class BarModel:
        def __init__(self, **kwargs):
            pass

    def __init__(self):
        self.arguments = {'foo': 'eggs', 'bar': 'ham'}

    def test_match_call_signature(self):
        expected = {'foo': 'eggs'}
        arguments = BaseTestCase._match_call_signature(callable_=self.FooModel,
                                                       arguments=self.arguments)
        assert_dict_equal(arguments, expected)

    def test_match_call_signature_arbitrary_arguments(self):
        arguments = BaseTestCase._match_call_signature(callable_=self.BarModel,
                                                       arguments=self.arguments)
        assert_dict_equal(arguments, self.arguments)

