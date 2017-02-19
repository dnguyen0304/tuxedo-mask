# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import validate


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

