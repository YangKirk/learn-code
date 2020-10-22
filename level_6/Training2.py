# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Training2.py
   Description :
   Author :       Kirk
   date：          2019/12/11
-------------------------------------------------
   Change Activity:
                   2019/12/11:
-------------------------------------------------
"""
__author__ = 'Kirk'

import datetime
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    return datetime.datetime.now()


f = now
print(f())
print(f.__name__)
