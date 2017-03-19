# -*- coding: utf-8 -*-

import logging

from nose.tools import assert_false, assert_true

from tuxedomask import utilities


class TestStackTraceFilter:

    def __init__(self):
        self.filter = None

    def setup(self):
        self.filter = utilities.StackTraceFilter()

    def test_include(self):
        log_record = logging.makeLogRecord(dict(exc_info=False))
        is_included = self.filter.filter(record=log_record)
        assert_true(is_included)

    def test_exclude(self):
        log_record = logging.makeLogRecord(dict(exc_info=True))
        is_included = self.filter.filter(record=log_record)
        assert_false(is_included)

