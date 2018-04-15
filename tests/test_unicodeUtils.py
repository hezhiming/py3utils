#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from unittest import TestCase

import py3utils


class TestUnicodeUtils(TestCase):
    def test_get_str(self):
        # ok
        data = '世界与中国'
        res = py3utils.UnicodeUtils.get_str(data.encode('gbk'))
        self.assertTrue(res == data)
