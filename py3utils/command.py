#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import subprocess

from py3utils.exceptions import CommandRunFailedException


class Command:
    def __init__(self):
        self._cmd_str = None

        self._p = None
        self._stdout = None
        self._stderr = None

    def run(self, cmd_str: str):
        """运行命令

        不返回 stdout 的内容给调用方

        :param cmd_str:
        :return:
        """
        self._cmd_str = cmd_str

        self._p = subprocess.Popen(self._cmd_str, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (self._stdout, self._stderr) = self._p.communicate()

        if self._p.returncode != 0:
            raise CommandRunFailedException('run %s failed. reason: %s' % (self._cmd_str, self._stderr))
