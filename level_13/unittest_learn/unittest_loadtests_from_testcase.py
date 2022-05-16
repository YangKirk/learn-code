# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ut1
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
from level_13.unittest_learn.reg.stringtests import StringTests
from level_13.unittest_learn.reg.numbertests import NumberTests
import unittest

if __name__ == '__main__':
    # 通过unittest.defaultTestLoader.loadTestsFromTestCase()管理test case
    st = unittest.defaultTestLoader.loadTestsFromTestCase(StringTests)
    nt = unittest.defaultTestLoader.loadTestsFromTestCase(NumberTests)
    # 将test case的实例通过unittest.TestSuite实例化为一个 test suite
    suite = unittest.TestSuite([st, nt])

    # 通过unittest.TextTestRunner().run()方法运行suite
    unittest.TextTestRunner().run(suite)
