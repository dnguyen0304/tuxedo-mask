# -*- coding: utf-8 -*-

import bcrypt

from sqlalchemy import orm

import tuxedomask
from . import TuxedoMaskBaseRepository
from tuxedomask import models, repositories


class TuxedoMaskUsersRepository(TuxedoMaskBaseRepository):

    def get_by_username(self, username, application):
        query = (
            self._db_context.query(models.Users)
                            .filter_by(applications_id=application.applications_id,
                                       username=username))
        try:
            user = query.one()
        except orm.exc.NoResultFound:
            message = ("""The username "{username}" does not match that of """
                       """an existing user's for the application with the """
                       """name "{application_name}".""")
            raise repositories.EntityNotFound(
                message.format(username=username,
                               application_name=application.name))

        return user

    def add(self, entity, by=None):
        hashed_password = self._hash_password(entity.password.encode('utf-8'))
        entity.password = hashed_password.decode('utf-8')
        super().add(entity=entity, by=by)

    @staticmethod
    def _hash_password(password):

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

        iterations = (tuxedomask.configuration['services']
                                              ['tuxedomask']
                                              ['bcrypt_cost_factor'])
        salt = bcrypt.gensalt(rounds=iterations)
        hashed_password = bcrypt.hashpw(password=password, salt=salt)
        return hashed_password

