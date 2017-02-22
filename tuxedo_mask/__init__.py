# -*- coding: utf-8 -*-

import logging.config

import common
from common.logging import loggers

__all__ = ['api',
           'clients',
           'configuration',
           'models',
           'repositories',
           'resources',
           'utilities',
           'views']

configuration = common.utilities.get_configuration(application_name=__name__)

logging.setLoggerClass(loggers.UnstructuredDataLogger)
logging.config.dictConfig(configuration['logging'])

