#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#


from __future__ import unicode_literals, absolute_import

from unittest import TestCase
import time
from datetime import datetime

from py3utils import TimeUtils, DatetimeUtils


class TestTimeUtils(TestCase):
    def test_get_current_timestamp(self):
        expected = time.time()
        actual = TimeUtils.get_current_timestamp()

        self.assertTrue(0 < expected - actual < 1)


class TestDatetimeUtils(TestCase):
    def test_get_current_local_dt(self):
        expected = datetime.now()
        actual = DatetimeUtils.get_current_local_dt()

        self.assertTrue(expected.day == actual.day and expected.hour == actual.hour)
