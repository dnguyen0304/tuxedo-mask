# -*- coding: utf-8 -*-

import logging

from nose.tools import assert_in, assert_is

from common.logging import loggers


class TestLoggingConfiguration:

    def test_default_logger_class(self):
        assert_is(logging.getLoggerClass(), loggers.UnstructuredDataLogger)

    def test_package_logger_exists(self):
        assert_in('tuxedomask', logging.Logger.manager.loggerDict)

