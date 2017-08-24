#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/4/16
# author:      he.zhiming
# 

from unittest import TestCase
import time
from datetime import datetime
from dateutil import tz
from py3utils.datetimeutil import TimeUtils, DEFAULT_FMT


class TestTimeUtils(TestCase):
    def setUp(self):
        self.utc_dt = datetime.now(tz.tzutc())
        self.local_dt = datetime.now(tz.tzlocal())
        self.ts = TimeUtils.current_timestamp()
        self.time_str = self.local_dt.strftime(DEFAULT_FMT)

    def tearDown(self):
        del self.utc_dt
        del self.local_dt
        del self.time_str

    def test_current_utc_datetime(self):
        actural = TimeUtils.current_utc_datetime()
        expected = self.utc_dt

        self.assertEqual(expected.year, actural.year)
        self.assertEqual(expected.day, actural.day)

    def test_current_local_datetime(self):
        local_dt = TimeUtils.current_local_datetime()

        self.assertEqual(self.local_dt.day, local_dt.day)

    def test_timestamp2str(self):
        time_str = TimeUtils.timestamp2str(self.ts, timezone=tz.tzlocal())
        self.assertEqual(time_str, self.time_str)

    def test_datetime2str(self):
        time_str = TimeUtils.datetime2str(self.local_dt)
        self.assertEqual(time_str, self.time_str)

    def test_timestamp2datetime(self):
        ts = TimeUtils.current_timestamp()

        dt = TimeUtils.timestamp2datetime(ts, timezone=tz.tzlocal())

        self.assertEqual(dt.day, self.local_dt.day)

    def test_convert_datetime(self):
        utc_dt = TimeUtils.current_utc_datetime()
        local_dt = TimeUtils.current_local_datetime()

        self.assertEqual(utc_dt.hour + 8, local_dt.hour)
