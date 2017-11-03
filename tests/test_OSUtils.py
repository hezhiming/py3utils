#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
# 

from __future__ import absolute_import, unicode_literals

import platform

from unittest import TestCase, skipUnless

from py3utils import OSUtils


def _is_windows():
    OS = platform.platform().lower()
    return OS.startswith('windows')


def _is_linux():
    OS = platform.platform().lower()
    return OS.startswith('linux')


class TestOSUtils(TestCase):
    @skipUnless(_is_windows(), 'must be windows')
    def test_is_windows(self):
        self.assertTrue(OSUtils.is_windows())

    @skipUnless(_is_linux(), 'must be linux')
    def test_is_linux(self):
        self.assertTrue(OSUtils.is_linux())

    def test_get_current_os(self):
        self.assertTrue(isinstance(OSUtils.get_current_os(), str))
