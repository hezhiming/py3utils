#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/4/16
# author:      he.zhiming
# 

from urllib import parse

__all__ = (
    "Url"
)


class Url:
    def __init__(self, url):
        self._pr = parse.urlparse(url)

    @property
    def scheme(self):
        return self._pr.scheme

    @property
    def netloc(self):
        return self._pr.netloc

    @property
    def path(self):
        return self._pr.path

    @property
    def query(self):
        return self._pr.query

    @property
    def fragment(self):
        return self._pr.fragment

    @classmethod
    def encode_query(cls, query_dict):
        """编码查询

        :param query_dict:
        :rtype: str
        :return: 编码后的字符串(utf8编码)
        """

        return parse.urlencode(query_dict)

    @classmethod
    def decode_query(cls, query_str):
        """解码查询字符串

        :param query_str:
        :rtype: list[tuple]
        :return: 解码后的Python对象
        """

        return parse.parse_qsl(query_str)

    @classmethod
    def quote_str(cls, string):
        """对含不安全字符的字符串转码"""

        return parse.quote(string)

    @classmethod
    def unquote_str(cls, quoted_str):
        """解码"""

        return parse.unquote(quoted_str)

    @classmethod
    def defragment(cls, url):
        """去除url中的defragment"""

        return parse.urldefrag(url)
