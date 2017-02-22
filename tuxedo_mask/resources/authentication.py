# -*- coding: utf-8 -*-

import bcrypt

import flask
import flask_httpauth

from tuxedo_mask import services

authentication = flask_httpauth.HTTPBasicAuth()


@authentication.get_password
def get_password(username):

    service = services.TuxedoMaskService.from_configuration()
    application = service.applications.get_by_name('tuxedo_mask')
    user = service.users.get_by_username(username=username,
                                         application=application)

    flask.g.password_salt = user.password[:29]

    return user.password


@authentication.hash_password
def hash_password(password):

    salt = flask.g.password_salt.encode('utf-8')
    hashed_password = (
        bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
              .decode('utf-8'))

    return hashed_password

