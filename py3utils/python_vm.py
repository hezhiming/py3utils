#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/2/14
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import platform


class PythonVmUtils:
    @classmethod
    def get_python_vm_str(cls) -> str:
        return platform.python_version()

    @classmethod
    def is_py3(cls):
        return cls.get_python_vm_str().startswith('3')

    @classmethod
    def is_py2(cls):
        return cls.get_python_vm_str().startswith('2')
