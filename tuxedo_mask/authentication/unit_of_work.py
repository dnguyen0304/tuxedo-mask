# -*- coding: utf-8 -*-


class UnitOfWork:

    def __init__(self, repositories, db_context, logger):
        self._db_context = db_context
        self._logger = logger

        for name, class_ in repositories.items():
            repository = class_(db_context=self._db_context, logger=self._logger)
            setattr(self, '_' + name, repository)

    @property
    def applications(self):
        return self._applications_repository

    @property
    def users(self):
        return self._users_repository

    def dispose(self):
        self._db_context.dispose()

