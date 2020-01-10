# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     class_vector
   Description :
   Author :       Kirk
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""
__author__ = 'Kirk'


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        """

        Args: self, other
            other:
                    __cmp__: 比较运算
                    __call__: 函数调用
                    __add__: 加运算
                    __sub__: 减运算
                    __mul__: 乘运算
                    __truediv__: 除运算
                    __mod__: 求余运算
                    __pow__: 乘方

        Returns:

        """
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vector(self.a - other.b, self.b - other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1 - v2)
