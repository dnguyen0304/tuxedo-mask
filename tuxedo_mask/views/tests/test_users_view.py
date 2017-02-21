# -*- coding: utf-8 -*-

import base64
import re

import marshmallow
from nose.tools import assert_equal, assert_in, assert_true, raises

from . import BaseTestCase
from tuxedo_mask import models, views
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


class TestUsersView(BaseTestCase):

    @property
    def _Model(self):
        return models.Users

    @property
    def _View(self):
        return views.UsersView

    @property
    def fields(self):
        return ['username', 'password']

    @property
    def values(self):
        encoded_password = (
            base64.b64encode('Foo45678'.encode('utf-8')).decode('utf-8'))
        return ['foo', encoded_password]

    def help_validate(self, field, value, keyword):
        value = base64.b64encode(value.encode('utf-8')).decode('utf-8')
        super().help_validate(field=field, value=value, keyword=keyword)

    def test_username_minimum_length(self):
        self.help_validate(field='username',
                           value=str(),
                           keyword='length')

    def test_username_maximum_length(self):
        self.help_validate(field='username',
                           value='x' * 50,
                           keyword='length')

    def test_password_minimum_length(self):
        self.help_validate(field='password',
                           value='Foo4567',
                           keyword='length')

    def test_password_contains_lowercase_characters(self):
        self.help_validate(field='password',
                           value='FOO45678',
                           keyword='lowercase')

    def test_password_contains_uppercase_characters(self):
        self.help_validate(field='password',
                           value='foo45678',
                           keyword='uppercase')

    def test_password_contains_numeric_characters(self):
        self.help_validate(field='password',
                           value='Fooooooo',
                           keyword='numeric')

