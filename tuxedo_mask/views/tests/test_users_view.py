# -*- coding: utf-8 -*-

import re

import marshmallow
from nose.tools import assert_equal, assert_in, assert_true, raises

from tuxedo_mask.views import users_view


class TestContainsAtLeast:

    def test(self):
        value = 'foo'
        validator = users_view.ContainsAtLeast(choices=['f'])
        assert_equal(validator(value=value), value)

    @raises(marshmallow.exceptions.ValidationError)
    def test_raises_validation_error(self):
        value = 'foo'
        validator = users_view.ContainsAtLeast(choices=['x'])
        validator(value=value)

    def test_formats_error_message(self):
        value = 'foo'
        choices = ['f']
        error_pattern = 'input (.+) choices (.+) count (\d+)'
        error = 'input {input} choices {choices} count {count}'

        validator = users_view.ContainsAtLeast(choices=choices, error=error)
        error_message = validator._format_error(value=value)

        result = re.match(pattern=error_pattern, string=error_message)
        assert_true(result)
        assert_equal(result.groups()[0], value)
        assert_in(choices[0], result.groups()[1])
        assert_equal(result.groups()[2], '1')

