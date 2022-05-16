# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_learning
   Description :  
   Author :       kirk
   date：          2022/5/15
-------------------------------------------------
   Change Activity:
                   2022/5/15
-------------------------------------------------
"""
import unittest


class Demo(unittest.TestCase):  # 必须继承于unittest.TestCase类

    def setUp(self) -> None:  # 每个测试方法执行前执行一次
        print("这是每一个test case开始的初始化方法")

    def tearDown(self) -> None:  # 每个测试方法执行结束后执行一次
        print("这是每一个test case结束的初始化方法\n")

    @classmethod
    def setUpClass(cls):  # 整个测试执行前执行一次
        print("这是setUpClass方法，优先级在setUp方法之前")

    @classmethod
    def tearDownClass(cls) -> None:  # 整个测试执行结束后执行一次
        print("这是tearDownClass方法，优先级在最后的最后，所有测试结束以后执行")

    @staticmethod
    def test_case2():
        print("这是test_case2方法")

    @staticmethod
    def testLogin():
        print("这是testLogin方法")

    @staticmethod
    def testBogin():
        print("这是test Bogin方法")

    @staticmethod
    def test_case1():
        print("这是test_case1方法")


if __name__ == "__main__":
    print("测试已经开始，准备调用")
    unittest.main()
