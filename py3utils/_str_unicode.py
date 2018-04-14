#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2018/3/2
# author:      he.zhiming
#

from __future__ import unicode_literals, absolute_import


class UnicodeUtils:
    @classmethod
    def get_str(cls, bytes_str: bytes, *, try_decoders=('utf-8', 'gbk', 'utf-16'))->str:
        if not bytes_str:
            return ''

        if isinstance(bytes_str, (str,)):
            return bytes_str

        for decoder in try_decoders:
            try:
                unicode_str = bytes_str.decode(decoder)
            except UnicodeDecodeError as e:
                pass
            else:
                return unicode_str

        raise UnicodeDecodeError('decode bytes failed. use decoders: %s' % try_decoders)
