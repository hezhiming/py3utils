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
        with self.assertRaises(py3utils.Py3UtilsException):
            py3utils.Asserts.not_null(None)

    def test_not_empty(self):
        empty_values = (0, '', 0.0, None,)

        for value in empty_values:
            with self.assertRaises(py3utils.Py3UtilsException):
                py3utils.Asserts.not_empty(value)

    def test_is_true(self):
        # None
        value = None
        with self.assertRaises(py3utils.Py3UtilsException):
            py3utils.Asserts.is_true(value)

        # False
        expr2 = False
        with self.assertRaises(py3utils.Py3UtilsException):
            py3utils.Asserts.is_true(expr2)

        # True
        expr3 = True
        actual = py3utils.Asserts.is_true(expr3)
        self.assertTrue(actual == expr3)

        # True expr
        expr4 = ('' is None)
        with self.assertRaises(py3utils.Py3UtilsException):
            py3utils.Asserts.is_true(expr4)
        expr5 = (not '')
        actual5 = py3utils.Asserts.is_true(expr5)
        self.assertTrue(actual5 == expr5)
