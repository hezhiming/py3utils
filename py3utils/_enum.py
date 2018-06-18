#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/6/18
# author:      he.zhiming
#

"""
本文件描述:
"""

from __future__ import unicode_literals, absolute_import

import functools


class BaseEnum:
    @classmethod
    @functools.lru_cache(maxsize=1024)
    def values(cls):
        d = cls.__dict__
        return [v
                for k, v in d.items()
                if (not k.startswith('_')) and k.isupper()]
