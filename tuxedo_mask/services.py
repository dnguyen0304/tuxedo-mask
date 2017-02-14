# -*- coding: utf-8 -*-

import base64

import bcrypt
from common import database
from sqlalchemy import orm

from . import models
from tuxedo_mask import configuration


def verify_credentials(encoded, scope):

    """
    Verify the credentials.

    The credentials must be encoded according to the Basic Access
    Authentication scheme described in RFC 1945 [1] [2].

    Parameters
    ----------
    encoded : bytes
        Encoded username and password.
    scope : models.Applications
        Namespace within which to search for the user.

    Returns
    -------
    bool
        True if the username and password match those of an existing
        user's. False if the username matches that of an existing
        user's, but the password does not.

    Raises
    ------
    ValueError
        If the username does not match that of an existing user's.
    """

    db_context_factory = database.DBContextFactory(
        connection_string=configuration['databases']['postgresql']['connection_string'])
    db_context = db_context_factory.create()

    username, password = decode_credentials(encoded=encoded)
    query = db_context.query(models.ApplicationsUsers).filter_by(
        application_id=scope.application_id,
        username=username)

    try:
        user = query.one()
    except orm.exc.NoResultFound:
        message = ("""The username "{username}" does not match that of an """
                   """existing user's within the scope of the application """
                   """"{application_name}".""")
        raise ValueError(
            message.format(username=username, application_name=scope.name))

    passes_verification = bcrypt.checkpw(
        password=password,
        hashed_password=user.password.encode('utf-8'))

    return passes_verification


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
        Decoded username and password. Two-element tuple of strings.
        The first element is the decoded username. The second element
        is the decoded, unhashed password.

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

