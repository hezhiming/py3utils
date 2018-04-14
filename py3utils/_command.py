#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import subprocess

from py3utils._exceptions import CommandRunFailedException

from py3utils._str_unicode import UnicodeUtils


class CommandRunner:
    def __init__(self):
        """

        Usage:
            CommandRunner().run(some_cmd_str)

        :return:
        """
        self._cmd_str = None

        self._p = None
        self._stdout = None
        self._stderr = None

    def run(self, cmd_str: str, *, use_pipe=True):
        """运行命令

        不返回 stdout 的内容给调用方

        :param cmd_str:
        :return:
        """
        self._cmd_str = cmd_str

        if use_pipe:
            self._p = subprocess.Popen(self._cmd_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            self._p = subprocess.Popen(self._cmd_str, shell=True)

        (self._stdout, self._stderr) = self._p.communicate()

        if self._p.returncode != 0:
            raise CommandRunFailedException('run command failed(%s). reason: %s' % (
                self._cmd_str, UnicodeUtils.get_str(self._stderr)))
        else:
            return UnicodeUtils.get_str(self._stdout)
