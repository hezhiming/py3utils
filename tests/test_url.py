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

    # def test_quote_str(self):
    #
    #
    # def test_unquote_str(self):
    #     self.fail()

    def test_defragment(self):
        defraged_url = Url.defragment(self.url_str).url
        url_obj = Url(defraged_url)

        self.assertEqual(url_obj.fragment, '')
