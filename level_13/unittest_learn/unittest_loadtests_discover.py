# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_loadtests_discover
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
import unittest


# 获取所有的test case
def get_all_cases():
    for case_dir in ['reg', 'smoke', 'sys']:
        dis_ = unittest.defaultTestLoader.discover(r'../unittest_learn/' + case_dir, pattern='*.py')
        suite_ = unittest.TestSuite(dis_)
    return suite_


if __name__ == '__main__':
    # 通过discover()方法运行reg回归测试脚本
    dis = unittest.defaultTestLoader.discover(r'./reg', pattern='*.py')
    suite = unittest.TestSuite(dis)
    unittest.TextTestRunner().run(suite)

    # 执行所有的test case(reg/smoke/sys)
    # unittest.TextTestRunner().run(get_all_cases())
