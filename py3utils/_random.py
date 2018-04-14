#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/22
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import random


class RandomUtils:
    @classmethod
    def get_random_float(cls) -> float:
        """调整标准库命名

        提示调用者, 会返回一个float

        :return:
        """
        return random.random()

    @classmethod
    def get_random_int(cls, left, right) -> int:
        """从一个范围里, 取一个int  [left, right]

        :param left:
        :param right:
        :return:
        """
        return random.randint(left, right)
