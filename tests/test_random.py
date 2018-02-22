#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/22
# author:      he.zhiming
#
from __future__ import unicode_literals, absolute_import

from unittest import TestCase

from py3utils import RandomUtils


class TestRandomUtils(TestCase):
    def test_get_random_float(self):
        print(RandomUtils.get_random_float())

    def test_get_random_int(self):
        print(RandomUtils.get_random_int(1, 10))
