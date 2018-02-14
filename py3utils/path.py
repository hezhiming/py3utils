#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/11/4
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import

import os
import shutil


class Path:
    """对路径的抽象操作

    使用:
        p = Path("/a/b/c")
        if p.is_dir():

        p.mkdir()

        p.cp('/b/c/destdir')
    """

    def __init__(self, pathstr: str):
        self._pathstr = pathstr
        self._abspath = os.path.abspath(pathstr)

    def get_parent(self):
        return Path(os.path.dirname(self._abspath))

    def get_childs(self):
        return [Path(c)
                for c in os.listdir(self._abspath)]

    def is_absolute(self):
        return os.path.isabs(self._pathstr)

    def is_dir(self):
        return os.path.isdir(self._abspath)

    def is_file(self):
        return os.path.isfile(self._abspath)

    def join(self, s):
        return Path(os.path.join(self._abspath, s))

    def get_basename(self):
        return os.path.basename(self._abspath)

    def get_extension(self):
        return os.path.splitext(self._abspath)[1]

    def get_filename(self):
        return os.path.split(self._abspath)[1]

    def is_exists(self):
        return os.path.exists(self._abspath)

    def ends_with(self, ext):
        return self._abspath.endswith(ext)

    def touch(self):
        if self.is_exists():
            return True

        open(self._abspath, mode='r', encoding='utf-8').close()

        return True

    def mkdir(self):
        if self.is_exists():
            return

        os.makedirs(self._abspath)

        return True

    def rm(self):
        if not self.is_exists():
            return

        if self.is_file():
            os.remove(self._abspath)
        if self.is_dir():
            shutil.rmtree(self._abspath)

    def mv(self, dest):
        shutil.move(self._abspath, dest)

    def cp(self, dest):
        if self.is_file():
            shutil.copyfile(self._abspath, dest)

        if self.is_dir():
            shutil.copytree(self._abspath, dest)


class File:
    def __init__(self, filestr: str):
        if not os.path.isfile(filestr):
            raise ValueError('must be a real file, now is %s' % filestr)

        self._filestr = os.path.abspath(filestr)
        self._statresult = os.stat(self._filestr)

    def get_size(self):
        return self._statresult.st_size

    def get_create_time(self):
        return self._statresult.st_ctime
