#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:   he.zhiming
#

"""定制本lib的异常体系"""

from __future__ import (absolute_import, unicode_literals)


class Py3UtilsException(Exception):
    pass


class CommandRunFailedException(Py3UtilsException):
    pass
