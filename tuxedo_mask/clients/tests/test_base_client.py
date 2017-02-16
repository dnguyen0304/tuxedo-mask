# -*- coding: utf-8 -*-

import base64

from nose.tools import assert_tuple_equal

from tuxedo_mask import clients


def test_parse_authorization_header():

    credentials = ('foo', 'bar')
    encoded = base64.b64encode(':'.join(credentials).encode('utf-8'))
    header = 'Basic ' + encoded.decode('utf-8')
    decoded = clients.BaseClient._parse_authorization_header(header)
    assert_tuple_equal(decoded, credentials)

