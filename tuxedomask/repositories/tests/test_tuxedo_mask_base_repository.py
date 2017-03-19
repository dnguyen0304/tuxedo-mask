# -*- coding: utf-8 -*-

from nose.tools import (assert_is_instance,
                        assert_is_none,
                        assert_is_not_none,
                        assert_true,
                        raises)

from tuxedomask import repositories


class MockEntity:
    pass


def test_set_sid():

    entity = MockEntity()
    entity.entity_sid = None
    repositories.TuxedoMaskBaseRepository._set_sid(entity=entity)

    assert_is_not_none(entity.entity_sid)


def test_set_sid_filter_protected_attributes():

    entity = MockEntity()
    entity._entity_sid = None
    entity.entity_sid = None
    repositories.TuxedoMaskBaseRepository._set_sid(entity=entity)

    assert_is_none(entity._entity_sid)
    assert_is_not_none(entity.entity_sid)


@raises(IndexError)
def test_set_sid_attribute_not_found():

    entity = MockEntity()
    repositories.TuxedoMaskBaseRepository._set_sid(entity=entity)


def test_generate_sid_return_type():

    sid = repositories.TuxedoMaskBaseRepository._generate_sid()
    assert_is_instance(sid, str)


def test_generate_sid_length():

    sid = repositories.TuxedoMaskBaseRepository._generate_sid()
    assert_true(len(sid) == 32)


def test_generate_sid_is_alphanumeric():

    sid = repositories.TuxedoMaskBaseRepository._generate_sid()
    assert_true(sid.isalnum())

