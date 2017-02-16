# -*- coding: utf-8 -*-

from nose.tools import assert_is_instance, assert_true

from tuxedo_mask import repositories


def test_unit_of_work_has_repository_attributes():

    class BaseRepository:
        def __init__(self, db_context, logger):
            pass

    class FooRepository(BaseRepository):
        pass

    class BarRepository(BaseRepository):
        pass

    my_repositories = {'foo_repository': FooRepository,
                       'bar_repository': BarRepository}
    unit_of_work = repositories.UnitOfWork(repositories=my_repositories,
                                           db_context=None,
                                           logger=None)

    for name, class_ in my_repositories.items():
        assert_true(hasattr(unit_of_work, '_' + name))
        assert_is_instance(getattr(unit_of_work, '_' + name), class_)

