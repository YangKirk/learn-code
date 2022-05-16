# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_loadtests_from_module
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
from level_13.unittest_learn.reg import stringtests as st, numbertests as nu
import unittest

if __name__ == '__main__':
    names = [st, nu]
    modules = []

    for item in names:
        # 通过unittest.defaultTestLoader.loadTestsFromModule()方法管理test case
        module = unittest.defaultTestLoader.loadTestsFromModule(st)
        modules.append(module)

    suite = unittest.TestSuite(modules)
    unittest.TextTestRunner().run(suite)
