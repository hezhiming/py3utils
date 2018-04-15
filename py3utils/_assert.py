#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import


class Asserts:
    @classmethod
    def not_null(cls, value, *, errmsg='value is None'):
        if value is None:
            raise TypeError(errmsg)

        return cls

    @classmethod
    def not_empty(cls, value, *, errmsg='value is empty'):
        if not value:
            raise TypeError(errmsg)

        return cls
