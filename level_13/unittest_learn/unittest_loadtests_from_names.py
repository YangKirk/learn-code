# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_loadtests_from_names
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
import unittest


def getFullTestCaseName(names):
    """
    获取符合条件的test case的名称，通常用于过滤smoke/sys/reg等测试
    :param names: 接收通过unittest.defaultTestLoader.getTestCaseNames()方法获取测试类中的test case名称列表
    :return: 符合条件的test case名称列表 --> return List
    """
    full_names = []
    for item in names:
        # 过滤条件，test case的名称中是否包含某些字符
        if 'Sub' in item:
            # 添加前缀路径
            full_names.append('reg.numbertests.NumberTests.' + item)

    return full_names


if __name__ == '__main__':
    # 方法一
    # 方法名最好写绝对路径或者不会变动的相对路径
    # names = ['level_13.unittest_learn.reg.numbertests.NumberTests.testSub',
    #          'level_13.unittest_learn.reg.stringtests.StringTests.testStr1']
    names_ = ['reg.numbertests.NumberTests.testSub',
              'reg.stringtests.StringTests.testStr1']
    # 通过unittest.defaultTestLoader.loadTestsFromNames()方法管理test case
    name_test = unittest.defaultTestLoader.loadTestsFromNames(names_)
    suite = unittest.TestSuite([name_test])
    unittest.TextTestRunner().run(suite)

    # 方法二
    from level_13.unittest_learn.reg.numbertests import NumberTests

    # 通过unittest.defaultTestLoader.getTestCaseNames()方法获取测试类中的test case名称列表
    names_ = unittest.defaultTestLoader.getTestCaseNames(NumberTests)
    # 定义并传入getFullTestCaseName方法，返回符合条件的test case 名称列表
    name_test = unittest.defaultTestLoader.loadTestsFromNames(getFullTestCaseName(names_))
    suite = unittest.TestSuite([name_test])
    unittest.TextTestRunner().run(suite)
