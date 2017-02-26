# -*- coding: utf-8 -*-

import logging

import bcrypt
import sqlalchemy
from common import database

from . import BaseService
from tuxedo_mask import configuration, repositories


class TuxedoMaskService(BaseService):

    _db_context_factory = database.DBContextFactory(
        connection_string=configuration['postgresql']['connection_string'])

    @classmethod
    def from_configuration(cls):
        logger = logging.getLogger(
            name=configuration['services']['tuxedo_mask']['logger_name'])
        db_context = cls._db_context_factory.create()
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

    @classmethod
    def get_connection_pool_status(cls):
        connection_pool = cls._db_context_factory._SessionFactory.get_bind().pool
        status = {'connection_pool_size': connection_pool.size(),
                  'connection_pool_overflow': connection_pool.overflow(),
                  'checked_in_connections': connection_pool.checkedin(),
                  'checked_out_connections': connection_pool.checkedout()}
        return status

