# -*- coding: utf-8 -*-

import logging

import bcrypt
import sqlalchemy
from common import database

from . import BaseService
from tuxedo_mask import configuration, repositories


class TuxedoMaskService(BaseService):

    @classmethod
    def from_configuration(cls):
        logger = logging.getLogger(
            name=configuration['services']['tuxedo_mask']['logger_name'])

        db_context_factory = database.DBContextFactory(
            connection_string=configuration['postgresql']['connection_string'])
        db_context = db_context_factory.create()

        my_repositories = {
            'applications_repository': repositories.TuxedoMaskApplicationsRepository,
            'users_repository': repositories.TuxedoMaskUsersRepository}

        return TuxedoMaskService(db_context=db_context,
                                 repositories=my_repositories,
                                 logger=logger)

    def _do_verify_credentials(self, username, password, scope):
        user = self.users.get_by_username(username, application=scope)
        passes_verification = bcrypt.checkpw(
            password=password.encode('utf-8'),
            hashed_password=user.password.encode('utf-8'))

        return passes_verification

    def commit(self):
        try:
            self._db_context.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self._db_context.rollback()
            raise repositories.EntityConflict(str(e))

    def dispose(self):
        self._db_context.close()

