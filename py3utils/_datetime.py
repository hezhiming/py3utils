#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/4/16
# author:      he.zhiming
# 

"""封装datetime"""

import time
from datetime import datetime
from dateutil import tz

DEFAULT_FMT = '%Y/%m/%d %H:%M:%S'


class TimeUtils:
    @classmethod
    def get_current_timestamp(cls):
        return int(time.time())

    @classmethod
    def get_current_timestamp_ms(cls):
        return int(time.time() * 1000)

    @classmethod
    def current_utc_datetime(cls):
        return datetime.now(tz.tzutc())

    @classmethod
    def current_local_datetime(cls):
        return datetime.now(tz.tzlocal())

    @classmethod
    def timestamp2str(cls, ts, timezone=None, fmt=None):
        if timezone is None:
            timezone = tz.tzlocal()

        if fmt is None:
            fmt = DEFAULT_FMT

        dt = cls.timestamp2datetime(ts, timezone=timezone)

        return cls.datetime2str(dt, fmt=fmt)

    @classmethod
    def datetime2str(cls, dt, fmt=None):
        if fmt is None:
            fmt = DEFAULT_FMT

        return dt.strftime(fmt)

    @classmethod
    def timestamp2datetime(cls, ts, timezone=None):
        if timezone is None:
            timezone = tz.tzlocal()

        return datetime.fromtimestamp(ts, timezone)

    @classmethod
    def convert_datetime(cls, from_dt, timezone, offset_seconds):
        return from_dt.astimezone(tz.tzoffset(timezone, offset_seconds))

    @classmethod
    def timestr_to_timestamp(cls, time_str, fmt):
        dt = datetime.strptime(time_str, fmt)

        return int(dt.timestamp())

    @classmethod
    def timestamp_to_timestr(cls, ts, fmt):
        if ts < 0:
            raise ValueError('ts can not less than 0')

        dt = datetime.fromtimestamp(ts)

        return dt.strftime(fmt)
