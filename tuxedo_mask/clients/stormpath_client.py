# -*- coding: utf-8 -*-

import logging
import sys
import traceback

from stormpath.client import Client
from stormpath.error import Error as StormpathError

import tuxedo_mask
from . import BaseClient
from tuxedo_mask import repositories


class StormpathClient(BaseClient):

    @classmethod
    def from_configuration(cls):
        logger = logging.getLogger(
            name=tuxedo_mask.configuration['clients']['stormpath']['logger_name'])

        # Each application have should exactly one Stormpath Client. A
        # key reason is because this object manages cache to avoid
        # unnecessary API requests.
        stormpath_client = Client(
            api_key_id=tuxedo_mask.configuration['clients']['stormpath']['api_key_id'],
            api_key_secret=tuxedo_mask.configuration['clients']['stormpath']['api_key_secret'])

        my_repositories = {
            'applications_repository': repositories.StormpathApplicationsRepository,
            'users_repository': repositories.StormpathUsersRepository}

        return StormpathClient(db_context=stormpath_client,
                               repositories=my_repositories,
                               logger=logger)

    def _do_verify_credentials(self, username, password, scope):
        application = self.applications.get_by_name(name=scope.name)

        try:
            passes_verification = bool(
                application.authenticate_account(login=username, password=password))
        except StormpathError:
            passes_verification = False
            self._logger.exception(''.join(
                traceback.format_exception_only(*sys.exc_info()[:2])))

        return passes_verification

    def commit(self):
        pass

    def dispose(self):
        pass

