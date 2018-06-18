#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/4/15
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

from ._exceptions import Py3UtilsException


class Asserts:
    """
    替换语言内置的assert, python的assert在 -O 模式下没有作用, 而我们希望任何时候下都应该有作用

    使用:
        Asserts.not_null(var1).not_null(var2, errmsg='var2 is None').not_empty(var3)
    """

    @classmethod
    def not_null(cls, value, *, errmsg='value is None'):
        if value is None:
            raise Py3UtilsException(errmsg)

        return cls

    @classmethod
    def is_true(cls, bool_expr: bool, *, errmsg=''):
        if bool_expr is not True:
            raise Py3UtilsException(errmsg)

        return bool_expr

    @classmethod
    def not_empty(cls, value, *, errmsg='value is empty'):
        if not value:
            raise Py3UtilsException(errmsg)

        return cls
