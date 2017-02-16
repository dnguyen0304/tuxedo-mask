# -*- coding: utf-8 -*-

from sqlalchemy import orm

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

