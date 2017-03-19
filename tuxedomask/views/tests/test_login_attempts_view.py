# -*- coding: utf-8 -*-

import sys

from nose.tools import assert_equal, assert_true

from tuxedomask import views


def test_prepend_authentication_scheme():

    data = {'credentials': 'foo'}
    login_attempt = views.LoginAttemptsView().prepend_authentication_scheme(
        data=data)
    assert_true(login_attempt['credentials'].startswith('Basic '))


def test_prepend_authentication_scheme_fails_silently():

    try:
        views.LoginAttemptsView().prepend_authentication_scheme(data=dict())
    except KeyError as e:
        test_name = sys._getframe(0).f_code.co_name
        e_name = e.__class__.__name__
        message = '{test_name}() should not raise {e_name}.'

        raise AssertionError(
            message.format(test_name=test_name, e_name=e_name))


def test_prepend_authentication_scheme_does_not_mutate_inplace():

    data = {'credentials': 'foo'}
    views.LoginAttemptsView().prepend_authentication_scheme(data=data)
    assert_equal(data['credentials'], 'foo')

