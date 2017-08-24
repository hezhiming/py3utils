#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2017/4/16
# author:      he.zhiming
# 

from unittest import TestCase
from py3utils import Url


class TestUrl(TestCase):
    def setUp(self):
        self.url_str = 'https://www.baidu.com/path/to/here?q1=v1&q2=v2#frag'
        self.url = Url(self.url_str)

    def tearDown(self):
        del self.url_str
        del self.url

    def test_scheme(self):
        self.assertEqual(self.url.scheme, 'https')

    def test_netloc(self):
        self.assertEqual(self.url.netloc, 'www.baidu.com')

    def test_path(self):
        self.assertEqual(self.url.path, '/path/to/here')

    def test_query(self):
        self.assertEqual(self.url.query, 'q1=v1&q2=v2')

    def test_fragment(self):
        self.assertEqual(self.url.fragment, 'frag')

    def test_encode_query(self):
        query_dict = Url.decode_query(self.url.query)
        query_str = Url.encode_query(query_dict)

        self.assertEqual(query_str, self.url.query)

    def test_decode_query(self):
        query_str = self.url.query
        query_dict = Url.decode_query(query_str)

        self.assertEqual(query_dict, [('q1', 'v1'), ('q2', 'v2')])

    def test_escape_str(self):
        expected = '%20%20'
        actual = Url.escape_str('  ')

        self.assertEqual(expected, actual)

    def test_join_path(self):
        """测试URL合并"""

        base = '/a/b/'
        path = 'c/d'

        expected = '/a/b/c/d'
        actual = Url.join_path(base, path)

        self.assertEqual(expected, actual)


