#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
#

import os

from .constants import (WrongArgumentError)


class PathUtils:
    @classmethod
    def get_file_extension(cls, p):
        if not os.path.isfile(p):
            raise WrongArgumentError('must be a file')

        return os.path.splitext(p)[1]

    @classmethod
    def get_head(cls, p):
        return os.path.split(p)[0]

    @classmethod
    def get_tail(cls, p):
        return os.path.split(p)[1]

    @classmethod
    def join_path(cls, base, p):
        """合并路径

        假设:
            1. base是这样的: /a/b/
            2. p的形式不确定

        :param base:
        :type p: str
        :param p:
        :return:
        """

        base_abs_path = os.path.abspath(base)
        if p.startswith('/'):
            return os.path.join(base_abs_path, p[1:])
        else:
            return os.path.join(base_abs_path, p)
