#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import logging
import logging.config


class LogFactory:
    _LOG_CONFIG_DICT = {

    }

    logging.config.dictConfig(_LOG_CONFIG_DICT)

    @classmethod
    def get_logger(cls, logger_name) -> logging.Logger:
        return logging.getLogger(logger_name)


DEBUGGER = LogFactory.get_logger('debugger')
CONSOLE_LOGGER = LogFactory.get_logger('console_logger')
