# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     class_animal
   Description :
   Author :       Kirk
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""
__author__ = 'Kirk'


class Animal:
    def __init__(self):
        self.animal = "animal"

    def run(self):
        print("{} is running...".format(self.animal))


class Dog(Animal):
    def __init__(self):
        self.animal = "Dog"

    def run(self):
        print('{} is running...'.format(self.animal))

    def eat(self):
        print('%s is eating meat...' % self.animal)


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


# dog = Dog()
# dog.run()
# dog.eat()
# cat = Cat("cat")
# cat.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
