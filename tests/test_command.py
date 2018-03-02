#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

from unittest import TestCase, skipUnless
import platform

from py3utils.exceptions import CommandRunFailedException
from py3utils import CommandRunner


def _is_linux():
    return 'linux' in platform.platform().lower()


class TestCommand(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.runner = CommandRunner()

    @skipUnless(_is_linux(), 'need linux')
    def test_run_raise_error(self):
        cmd = 'lssss -la'

        with self.assertRaises(CommandRunFailedException):
            self.runner.run(cmd)

    @skipUnless(_is_linux(), 'need linux')
    def test_run_success(self):
        cmd = 'ls -la ~'

        self.runner.run(cmd)
