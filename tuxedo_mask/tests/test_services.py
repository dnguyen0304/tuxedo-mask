# -*- coding: utf-8 -*-

import base64

from nose.tools import assert_tuple_equal

from tuxedo_mask import services


def test_decode_credentials():

    credentials = ('foo', 'bar')
    encoded = base64.b64encode(':'.join(credentials).encode('utf-8'))
    decoded = services.decode_credentials(encoded)
    assert_tuple_equal(decoded, credentials)

