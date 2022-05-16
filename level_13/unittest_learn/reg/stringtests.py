# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stringtests
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
import unittest


class StringTests(unittest.TestCase):

    def testStr1(self):
        self.assertIn('hello', 'hello world')

    def testStr2(self):
        self.assertIn('hello', 'kirk')

