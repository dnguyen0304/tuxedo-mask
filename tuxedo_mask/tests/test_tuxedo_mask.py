# -*- coding: utf-8 -*-

import logging

from nose.tools import assert_in, assert_is

from common.logging import loggers


def test_global_logger_class():

    assert_is(logging.getLoggerClass(), loggers.UnstructuredDataLogger)


def test_package_logger_exists():

    assert_in('tuxedo_mask', logging.Logger.manager.loggerDict)

