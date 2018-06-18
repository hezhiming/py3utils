#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#

"""时间/日期操作

默认是以秒为单位, 如果使用其他单位, 则会在API命名上特别指出
"""

from __future__ import unicode_literals, absolute_import

import time
from datetime import datetime
from datetime import date


class TimeUtils:
    @classmethod
    def get_current_timestamp(cls):
        return int(time.time())

    @classmethod
    def get_current_timestamp_ms(cls):
        return int(time.time() * 1000)

    @classmethod
    def get_today_zero_start_timestamp(cls):
        today = date.today()
        timetuple = today.timetuple()

        return time.mktime(timetuple)


class DatetimeUtils:
    @classmethod
    def get_current_local_dt(cls):
        return datetime.now()

    @classmethod
    def get_current_utc_dt(cls):
        return datetime.utcnow()

    @classmethod
    def convert_timestamp_to_local_dt(cls, timestamp):
        return datetime.fromtimestamp(timestamp)

    @classmethod
    def convert_timestamp_to_utc_dt(cls, timestamp):
        return datetime.utcfromtimestamp(timestamp)
