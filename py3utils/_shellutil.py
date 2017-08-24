#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/4/16
# author:      he.zhiming
#

import sys
import platform


class ShellUtils:
    PLATFORM = platform.platform().lower()

    @classmethod
    def is_windows(cls):
        return cls.PLATFORM.startswith('windows')

    @classmethod
    def is_linux(cls):
        return cls.PLATFORM.startswith('linux')

    @classmethod
    def get_linux_dist_info(cls):
        """获取Linux发行版信息"""

        return '-'.join(platform.linux_distribution())

    @classmethod
    def get_linux_kernel_info(cls):
        """获取Linux内核信息"""

        return platform.platform()

    @classmethod
    def get_python_vm_info(cls):
        """获取Python虚拟机版本信息"""

        return platform.python_version()

    @classmethod
    def get_cpu_arch(cls):
        """获取CPU架构"""

        return platform.machine()
