# -*- coding: utf-8 -*-

from . import BaseRepository


class StormpathBaseRepository(BaseRepository):

    def get(self, entity_id):
        raise NotImplementedError

    def remove(self, entity):
        raise NotImplementedError

    def search(self, predicate):
        raise NotImplementedError

