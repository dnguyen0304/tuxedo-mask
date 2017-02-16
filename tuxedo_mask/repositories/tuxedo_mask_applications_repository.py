# -*- coding: utf-8 -*-

from sqlalchemy import orm

from . import TuxedoMaskBaseRepository
from tuxedo_mask import models, repositories


class TuxedoMaskApplicationsRepository(TuxedoMaskBaseRepository):

    def get_by_name(self, name):
        query = self._db_context.query(models.Applications) \
                                .filter_by(name=name)
        try:
            application = query.one()
        except orm.exc.NoResultFound:
            message = ("""The name "{name}" does not match that of an """
                       """existing application's.""")
            raise repositories.EntityNotFound(message.format(name=name))

        return application

