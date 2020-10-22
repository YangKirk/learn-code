# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Training4
   Description :
   Author :       Kirk
   date：          2019/12/27
-------------------------------------------------
   Change Activity:
                   2019/12/27:
-------------------------------------------------
"""
__author__ = 'Kirk'


# private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
class Student:
    def __init__(self):
        self.__name = None
        self.__score = None

    def _private_1(self):
        return 'Hello, %s' % self.__name

    def _private_2(self):
        return 'Hi, your score is %s' % self.__score

    def greeting(self):
        if len(self.__name) > 3:
            return self._private_1()
        else:
            return self._private_2()

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student()
bart.set_name('Bot')
bart.set_score(59)
print(bart.greeting())
print(bart.get_score())
print(bart.get_name())
