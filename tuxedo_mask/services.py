# -*- coding: utf-8 -*-

import base64

import bcrypt

from tuxedo_mask import configuration


def decode_credentials(encoded):

    """
    Decode credentials.

    The credentials must be encoded according to the Basic Access
    Authentication scheme described in RFC 1945 [1] [2].

    Parameters
    ----------
    encoded : bytes
        Encoded username and password.

    Returns
    -------
    tuple
        Decoded username and password. Two-element tuple. The first
        element is the decoded username. The second element is the
        decoded, unhashed password.

    References
    ----------
    .. [1] Berners-Lee, et al., "Access Authentication",
       https://tools.ietf.org/html/rfc1945#section-11
    .. [2] Franks, et al., "Basic Authentication Scheme",
       https://tools.ietf.org/html/rfc2617#section-2
    """

    decoded = base64.b64decode(encoded).decode('utf-8')
    username, password = decoded.split(':')
    return username, password


def hash_password(password):

    """
    Hash the password.

    The underlying hashing algorithm is bcrypt.

    Parameters
    ----------
    password : bytes
        Decoded and unhashed password.

    Returns
    -------
    bytes
        Hashed password.
    """

    iterations = configuration['components']['hashing']['iterations']
    salt = bcrypt.gensalt(rounds=iterations)
    hashed_password = bcrypt.hashpw(password=password, salt=salt)
    return hashed_password

