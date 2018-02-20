#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/20
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import sys

from py3utils import Command

COMMAND_RUNNER = Command()


def _run_pytest():
    cmd = 'py.test ./tests/'

    COMMAND_RUNNER.run(cmd)


def _run_flake8():
    cmd = 'flake8 py3utils/'

    COMMAND_RUNNER.run(cmd)


def main():
    _run_pytest()
    _run_flake8()
    return 0


if __name__ == '__main__':
    sys.exit(main())
