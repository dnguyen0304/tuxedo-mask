# -*- coding: utf-8 -*-

import base64
import string

import marshmallow
from marshmallow import fields, validate

from . import BaseView
from tuxedo_mask import models


class ContainsAtLeast(validate.Validator):

    default_message = ("""The input must contain at least {count} of the """
                       """elements in {choices}.""")

    def __init__(self, choices, error=None):

        """
        Validator that succeeds if the input contains enough of the
        specified elements.

        Parameters
        ----------
        choices : iterable
            See the marshmallow.validate.OneOf documentation for more
            details.
        error : str, optional
            See the marshmallow.validate.OneOf documentation for more
            details. Defaults to ContainsAtLeast.default_message.

        See Also
        --------
        marshmallow.validate.OneOf
        """

        self.choices = choices
        self.choices_text = ', '.join(str(choice) for choice in self.choices)
        self.count = 1
        self.error = error or self.default_message

    def _format_error(self, value):
        return self.error.format(input=value,
                                 choices=self.choices_text,
                                 count=self.count)

    # import timeit
    #
    # # Under the given conditions, this algorithm performs
    # # approximately 15% to 20% faster than one implementing list
    # # comprehensions does.
    # timeit.repeat(setup="""import string""",
    #               stmt="""set('Hello, World!').intersection(string.ascii_lowercase)""",
    #               repeat=3,
    #               number=1000000)
    def __call__(self, value):
        if not set(value).intersection(self.choices):
            message = self._format_error(value=value)
            raise marshmallow.exceptions.ValidationError(message)
        return value


error_messages = {
    'username': {
        'length': """The username must be between {min} and {max} """
                  """characters in length, inclusive. You specified """
                  """"{input}"."""
    },
    'password': {
        'minimum_length': """The password must be at least {min} """
                          """characters in length.""",
        'lowercase_characters': """The password must contain at least """
                                """{count} lowercase character.""",
        'uppercase_characters': """The password must contain at least """
                                """{count} uppercase character.""",
        'numeric_characters': """The password must contain at least """
                              """{count} numeric character."""
    }
}


class _UsersView(marshmallow.Schema):

    users_sid = fields.String(dump_only=True)
    username = fields.String(
        required=True,
        validate=[
            validate.Length(min=1,
                            max=32,
                            error=error_messages['username']['length'])])
    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=8,
                            error=error_messages['password']['minimum_length']),
            ContainsAtLeast(choices=string.ascii_lowercase,
                            error=error_messages['password']['lowercase_characters']),
            ContainsAtLeast(choices=string.ascii_uppercase,
                            error=error_messages['password']['uppercase_characters']),
            ContainsAtLeast(choices=string.digits,
                            error=error_messages['password']['numeric_characters'])],
        load_only=True)

    @marshmallow.pre_load
    def decode_password(self, data):
        data_ = data.copy()
        try:
            data_['password'] = base64.b64decode(data_['password'])
        except KeyError:
            pass
        return data_


class UsersView(BaseView, _UsersView):

    _Model = models.Users

