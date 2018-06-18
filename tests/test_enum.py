#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/6/18
# author:      he.zhiming
#

"""
本文件描述:
"""

from unittest import TestCase

import py3utils


class DirectionEnum(py3utils.BaseEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class TestBaseEnum(TestCase):
    def test_values_is_list(self):
        self.assertTrue(isinstance(DirectionEnum.values(), list))

    def test_values(self):
        e = [1, 2, 3, 4]
        actual = DirectionEnum.values()

        self.assertEqual(e, actual)

    def test_enum(self):
        actual = DirectionEnum.UP
        expected = 1

        self.assertEqual(actual, expected)
