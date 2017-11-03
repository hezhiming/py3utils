#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
# 

from __future__ import absolute_import, unicode_literals


class LibBaseException(Exception):
    pass

class WrongArgumentError(LibBaseException):
    pass
