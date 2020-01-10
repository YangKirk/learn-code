# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     global_local
   Description :
   Author :       Kirk
   date：          2020/1/2
-------------------------------------------------
   Change Activity:
                   2020/1/2:
-------------------------------------------------
"""
__author__ = 'Kirk'
"""
total = 0  # 这是一个全局变量


# 可写函数说明
def sum_two(arg1, arg2):
    # 返回2个参数的和.
    _total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", _total)
    return _total


# 调用sum_two函数
sum_two(10, 20)
print("函数外是全局变量 : ", total)
"""

"""
num = "这是一个全局变量，我不会被修改"


def outer():
    _num = 10  # 这是一个是函数内的局部变量

    def inner():
        nonlocal _num  # nonlocal关键字声明,仅修改函数嵌套内的局部变量
        _num = 100  # 这是一个函数内局部变量
        print(_num)

    inner()
    print(_num)


outer()
print(num)
"""
a = 10


def test(a):
    a = a + 1
    print(a)


test(a)  # 传入参数
print(a)  # 全局变量a 未发生改变
