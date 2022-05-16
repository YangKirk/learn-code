# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     numbertests
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
import unittest


class NumberTests(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(1, 1)

    def testSub(self):
        self.assertNotEqual(1, 1)
