#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/20
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import sys

from py3utils import CommandRunner

COMMAND_RUNNER = CommandRunner()


def _run_pytest():
    cmd = 'py.test --verbose ./tests/'

    COMMAND_RUNNER.run(cmd, use_pipe=False)


def _run_flake8():
    cmd = 'flake8 --verbose py3utils/'

    COMMAND_RUNNER.run(cmd, use_pipe=False)


def main():
    _run_pytest()
    _run_flake8()
    return 0


if __name__ == '__main__':
    sys.exit(main())
