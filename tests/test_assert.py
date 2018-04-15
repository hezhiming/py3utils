#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from unittest import TestCase

import py3utils


class TestAssert(TestCase):
    def test_not_null(self):
        with self.assertRaises(TypeError):
            py3utils.Asserts.not_null(None)

    def test_not_empty(self):
        empty_values = (0, '', 0.0, None,)

        for value in empty_values:
            with self.assertRaises(TypeError):
                py3utils.Asserts.not_empty(value)
