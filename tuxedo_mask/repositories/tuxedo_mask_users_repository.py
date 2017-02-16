# -*- coding: utf-8 -*-

import bcrypt

import sqlalchemy
from sqlalchemy import orm

import tuxedo_mask
from . import TuxedoMaskBaseRepository
from tuxedo_mask import models, repositories


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
                       """an existing user's within the scope of the """
                       """application "{application_name}".""")
            raise repositories.EntityNotFound(
                message.format(username=username,
                               application_name=application.name))

        return user

    def add(self, entity, by):
        hashed_password = self._hash_password(entity.password.encode('utf-8'))
        entity.password = hashed_password.decode('utf-8')
        try:
            super().add(entity=entity, by=by)
        except sqlalchemy.exc.IntegrityError:
            message = ("""There is already an existing user with the """
                       """username "{user_username}" for the application """
                       """with the name "{application_name}".""")
            raise repositories.EntityConflict(
                message.format(user_username=entity.username,
                               application_name=by.name))

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

        iterations = (tuxedo_mask.configuration['clients']
                                               ['tuxedo_mask']
                                               ['bcrypt_cost_factor'])
        salt = bcrypt.gensalt(rounds=iterations)
        hashed_password = bcrypt.hashpw(password=password, salt=salt)
        return hashed_password

