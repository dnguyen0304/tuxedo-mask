# -*- coding: utf-8 -*-

import abc


class EntityConflict(Exception):
    pass


class EntityNotFound(Exception):
    pass


class BaseRepository(metaclass=abc.ABCMeta):

    def __init__(self, db_context, logger):
        self._db_context = db_context
        self._logger = logger

    @abc.abstractmethod
    def get(self, entity_id):
        pass

    @abc.abstractmethod
    def add(self, entity, by=None):

        """
        Add the entity to the repository.

        Parameters
        ----------
        entity : models.Base subclass
            Domain model to be added.
        by : models.Base subclass, optional.
            Domain model performing the operation. Defaults to None.
        """

        pass

    @abc.abstractmethod
    def remove(self, entity):
        pass

    @abc.abstractmethod
    def search(self, predicate):
        pass

