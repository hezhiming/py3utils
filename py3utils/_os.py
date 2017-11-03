#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
# 

from __future__ import absolute_import, unicode_literals

import platform


class OSUtils:
    _CURRENT_OS = platform.platform().lower()

    _LINUX_MARK = 'linux'
    _WINDOWS_MARK = 'windows'

    @classmethod
    def is_windows(cls):
        return cls._CURRENT_OS.startswith(cls._WINDOWS_MARK)

    @classmethod
    def is_linux(cls):
        return cls._CURRENT_OS.startswith(cls._LINUX_MARK)

    @classmethod
    def get_current_os(cls):
        return cls._CURRENT_OS
