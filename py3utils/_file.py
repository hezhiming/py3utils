#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
# 

from __future__ import absolute_import, unicode_literals

import os


class FileUtils:
    @classmethod
    def get_extension(cls, filename):
        return os.path.splitext(filename)[1]
