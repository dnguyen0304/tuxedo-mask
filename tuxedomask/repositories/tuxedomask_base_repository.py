# -*- coding: utf-8 -*-

import random
import string

import sqlalchemy

from . import BaseRepository


class TuxedoMaskBaseRepository(BaseRepository):

    def get(self, entity_id):
        raise NotImplementedError

    def add(self, entity, by=None):
        if sqlalchemy.inspect(entity).transient:
            self._set_sid(entity)
        self._db_context.add(entity, by=by.applications_id)

    def remove(self, entity):
        raise NotImplementedError

    def search(self, predicate):
        raise NotImplementedError

    @staticmethod
    def _set_sid(entity):
        result = filter(lambda x: not x.startswith('_') and x.endswith('_sid'),
                        dir(entity))

        try:
            attribute = list(result)[0]
        except IndexError:
            message = """An SID attribute was not found on the entity <{}>."""
            raise IndexError(message.format(entity))
        else:
            setattr(entity,
                    attribute,
                    TuxedoMaskBaseRepository._generate_sid())

    @staticmethod
    def _generate_sid():
        valid_characters = string.ascii_letters + string.digits
        sid = ''.join(random.SystemRandom().choice(valid_characters)
                      for _
                      in range(32))
        return sid

