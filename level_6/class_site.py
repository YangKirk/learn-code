# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     class_site
   Description :
   Author :       Kirk
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""
__author__ = 'Kirk'


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错:外部不能调用私有方法
