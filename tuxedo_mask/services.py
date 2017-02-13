# -*- coding: utf-8 -*-

import base64


def decode_credentials(encoded):

    """
    Decode credentials.

    The credentials must be encoded according to the Basic Access
    Authentication scheme described in RFC 1945 [1] [2].

    Parameters
    ----------
    encoded : str
        Encoded username and password.

    Returns
    -------
    tuple
        Decoded username and password. Two-element tuple. The first
        element is the decoded username. The second element is the
        decoded, unencrypted password.

    References
    ----------
    .. [1] Berners-Lee, et al., "Access Authentication",
       https://tools.ietf.org/html/rfc1945#section-11
    .. [2] Franks, et al., "Basic Authentication Scheme",
       https://tools.ietf.org/html/rfc2617#section-2
    """

    credentials = base64.b64decode(encoded).decode('utf-8')
    username, password = credentials.split(':')
    return username, password

