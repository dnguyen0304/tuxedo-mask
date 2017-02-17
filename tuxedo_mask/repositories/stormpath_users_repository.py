# -*- coding: utf-8 -*-

import uuid

from . import StormpathBaseRepository, StormpathApplicationsRepository


class StormpathUsersRepository(StormpathBaseRepository):

    def add(self, entity):

        """
        Add the entity to the repository.

        Parameters
        ----------
        entity : models.Base subclass
            Domain model to be added.
        """

        applications_repository = StormpathApplicationsRepository(
            db_context=self._db_context,
            logger=self._logger)
        application = applications_repository.get_by_name(name='tuxedo_mask')

        # Account email addresses must be unique within a Directory.
        # Their formats are validated.
        properties = {'username': entity.username,
                      'password': entity.password,
                      'email': str(uuid.uuid4()) + '@mfitapp.io'}
        application.accounts.create(properties=properties)

