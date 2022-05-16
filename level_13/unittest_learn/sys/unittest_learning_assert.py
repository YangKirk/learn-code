# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_learning_assert
   Description :  
   Author :       kirk
   date：          2022/5/15
-------------------------------------------------
   Change Activity:
                   2022/5/15
-------------------------------------------------
"""
import unittest


class TestAssert(unittest.TestCase):

    def testFunc2(self):
        self.func1()    # 在测试方法中调用一个普通方法
        print("这是一个测试assertIn的方法")
        self.assertIn('d', 'abc')  # 判断d是否在abc中，不在就会报错
        print("这句话不会被执行")   # 断言测试结果为Fail，则后续语句不会被执行

    def testFunc1(self):
        print("这是一个测试assertNotIn的方法")
        self.assertNotIn('d', 'abc')  # 判断d是否不在abc中，在就会报错
        print("这句话可以执行")    # 断言测试结果为Pass，则后续语句会被执行

    def testFunc3(self):
        print("这是一个测试assertEqual的方法")
        self.assertEqual(1, 1)  # 判断两个元素是否相等,不相等会报错

    def testFunc4(self):
        print("这是一个测试assertNotEqual的方法")
        self.assertNotEqual(1, 2)  # 判断两个元素是否不相等,相等会报错

    def testFunc5(self):
        print("这是一个测试assertTrue的方法")
        self.assertTrue(1)  # 判断传入的元素是否为True,不为True则报错

    def testFunc6(self):
        print("这是一个测试assertFalse的方法")
        self.assertFalse([])  # 判断传入的元素是否为False，不为False报错

    @staticmethod
    def func1():
        print("这是一个普通方法，不是测试方法,通过测试方法内部调用执行")


if __name__ == '__main__':
    unittest.main()
