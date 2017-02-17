# -*- coding: utf-8 -*-

from . import StormpathBaseRepository
from tuxedo_mask import repositories


class StormpathApplicationsRepository(StormpathBaseRepository):

    def get_by_name(self, name):
        query = {'name': name}
        result = self._db_context.applications.search(query=query)

        try:
            application = result[0]
        except IndexError:
            message = ("""The name "{name}" does not match that of an """
                       """existing application's.""")
            raise repositories.EntityNotFound(message.format(name=name))

        return application

    def add(self, entity):

        """
        Add the entity to the repository.

        Parameters
        ----------
        entity : models.Base subclass
            Domain model to be added.
        """

        properties = {'name': entity.name, 'createDirectory': entity.name}
        self._db_context.applications.create(properties=properties)

