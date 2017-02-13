# -*- coding: utf-8 -*-

import base64

from nose.tools import assert_tuple_equal

from tuxedo_mask import services


def encode_credentials(username, password):

    credentials = username + ':' + password
    encoded = base64.b64encode(credentials.encode('utf-8'))
    return encoded


def test_decode_credentials():

    credentials = ('foo', 'bar')
    encoded = encode_credentials(*credentials)
    decoded = services.decode_credentials(encoded)
    assert_tuple_equal(decoded, credentials)

