# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     class_student_3
   Description :
   Author :       Kirk
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""
__author__ = 'Kirk'


class Student:
    name = ''
    age = 0
    score = ''
    __slot__ = ("name", "age")

    def __init__(self, name, age, score):
        self.student = "student"
        self.name = name
        self.age = age
        self.score = score

    def run(self):
        print("{} is running... {} is also running".format(self.student, self.name))
        print("He is {}".format(self.score))


class Boy(Student):
    def __init__(self, name, age, score):
        Student.__init__(self, name, age, score)

    def play_ball(self):
        print("{} loves play ball...".format(self.student))

    def one(self):
        print("{} is a {} {}...".format(self.name, self.age, self.student))
        print("His score is {}..".format(self.score))


x = Student("Kirk", "18", "100")

x.run()

s = Boy("Kirk", "18", "100")
s.play_ball()
s.one()
