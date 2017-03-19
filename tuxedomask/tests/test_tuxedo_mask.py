# -*- coding: utf-8 -*-

import json
import logging
import logging.handlers
import re

from common.logging import formatters, loggers
from nose.tools import (assert_equal,
                        assert_in,
                        assert_is,
                        assert_is_instance,
                        assert_is_not_none,
                        assert_true)

from tuxedomask import utilities


class TestLoggingConfiguration:

    def __init__(self):
        self.logger = None

    def setup(self):
        self.logger = logging.getLogger(name='tuxedomask')

    def test_default_logger_class(self):
        assert_is(logging.getLoggerClass(), loggers.UnstructuredDataLogger)

    def test_logger_exists(self):
        assert_in('tuxedomask', logging.Logger.manager.loggerDict)

    def test_logger_severity_level_is_debug(self):
        assert_equal(self.logger.level, logging.DEBUG)

    def test_handler_exists(self):
        assert_true(self.logger.handlers)
        assert_true(len(self.logger.handlers) == 2)

    def test_handler_type(self):
        assert_true(
            all(isinstance(handler, logging.handlers.TimedRotatingFileHandler)
                for handler
                in self.logger.handlers))

    def test_handler_severity_level(self):
        severity_levels = [handler.level for handler in self.logger.handlers]
        assert_in(logging.DEBUG, severity_levels)
        assert_in(logging.ERROR, severity_levels)

    def test_handler_encoding(self):
        assert_true(all(handler.encoding == 'utf-8'
                        for handler
                        in self.logger.handlers))

    def test_application_handler_has_stack_trace_filter(self):
        handler = self.get_application_handler()
        assert_true(handler.filters)
        assert_equal(len(handler.filters), 1)
        assert_is_instance(handler.filters[0], utilities.StackTraceFilter)

    def test_application_handler_has_json_formatter(self):
        handler = self.get_application_handler()
        assert_is_not_none(handler.formatter)
        assert_is_instance(handler.formatter, formatters.JsonFormatter)

    def test_application_handler_formatter_format_has_timestamp(self):
        serialized = self.help_test_application_handler_formatter_format()
        assert_in('timestamp', serialized)

    def test_application_handler_formatter_format_has_severity_level(self):
        serialized = self.help_test_application_handler_formatter_format()
        assert_in('severity_level', serialized)

    def test_application_handler_formatter_format_has_message(self):
        serialized = self.help_test_application_handler_formatter_format()
        assert_in('message', serialized)

    def test_application_handler_formatter_format_timestamp_format(self):
        handler = self.get_application_handler()
        assert_equal(handler.formatter.datefmt, '%Y-%m-%d %H:%M:%S')

    def test_application_handler_formatter_format_timestamp_includes_milliseconds(self):
        serialized = self.help_test_application_handler_formatter_format()
        match = re.search(pattern='\.\d{3}$', string=serialized['timestamp'])
        assert_true(match)

    def test_error_handler_has_simple_formatter(self):
        handler = self.get_error_handler()
        assert_is_not_none(handler.formatter)
        assert_is_instance(handler.formatter, logging.Formatter)

    def test_error_handler_formatter_format_has_timestamp(self):
        format_ = self.get_error_handler().formatter._style._fmt
        assert_in('%(asctime)s', format_)

    def test_error_handler_formatter_format_has_severity_level(self):
        format_ = self.get_error_handler().formatter._style._fmt
        assert_in('%(levelname)s', format_)

    def test_error_handler_formatter_format_has_message(self):
        format_ = self.get_error_handler().formatter._style._fmt
        assert_in('%(message)s', format_)

    def test_error_handler_formatter_format_timestamp_format(self):
        handler = self.get_error_handler()
        assert_equal(handler.formatter.datefmt, '%Y-%m-%d %H:%M:%S')

    def test_error_handler_formatter_format_timestamp_includes_milliseconds(self):
        format_ = self.get_error_handler().formatter._style._fmt
        assert_in('%(asctime)s.%(msecs)03d', format_)

    def get_application_handler(self):
        handler = next(filter(lambda x: x.level == logging.DEBUG,
                              self.logger.handlers))
        return handler

    def get_error_handler(self):
        handler = next(filter(lambda x: x.level == logging.ERROR,
                              self.logger.handlers))
        return handler

    def help_test_application_handler_formatter_format(self):
        handler = self.get_application_handler()
        log_record = logging.makeLogRecord({'levelname': 'severity_level',
                                            'msg': 'message'})
        serialized = json.loads(handler.formatter.format(record=log_record))
        return serialized

