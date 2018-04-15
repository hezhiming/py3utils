#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from unittest import TestCase
import unittest

import platform

import py3utils

_PLATFORM_STR = platform.platform().lower()


def _is_linux():
    return 'linux' in _PLATFORM_STR


def _is_windows():
    return 'win' in _PLATFORM_STR


class TestOS(TestCase):
    @unittest.skipUnless(_is_windows(), 'need windows')
    def test_is_windows(self):
        self.assertTrue(py3utils.OS.is_windows())

    @unittest.skipUnless(_is_linux(), 'need linux')
    def test_is_linux(self):
        self.assertTrue(py3utils.OS.is_linux())

    def test_get_current_os(self):
        res = py3utils.OS.get_current_os()

        self.assertTrue(len(res) > 0 and (isinstance(res, str)))
