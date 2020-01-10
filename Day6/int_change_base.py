# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Training3
   Description :
   Author :       Kirk
   date：          2019/12/27
-------------------------------------------------
   Change Activity:
                   2019/12/27:
-------------------------------------------------
"""
__author__ = 'Kirk'

# int的进制转换
a = "12345"
print(a)

b = int(a, base=16)
print(b, "\n", int(a, 8))


def int2(x, base=2):
    return int(x, base)


c = int2('10010')
print(c)
