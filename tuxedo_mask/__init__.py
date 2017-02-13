# -*- coding: utf-8 -*-

import logging.config

from common import utilities
from common.logging import loggers

configuration = utilities.get_configuration(application_name=__name__)

logging.setLoggerClass(loggers.UnstructuredDataLogger)
logging.config.dictConfig(configuration['components']['logging'])

