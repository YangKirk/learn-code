# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Training1
   Description :
   Author :       Kirk
   date：          2019/12/11
-------------------------------------------------
   Change Activity:
                   2019/12/11:
-------------------------------------------------
"""
__author__ = 'Kirk'


# Class :类
class Student(object):
    """
    object 是基类，所有类的父类
    此时是Student的父类
    """
    # 传入name、score到init函数中
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

