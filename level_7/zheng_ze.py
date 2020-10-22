# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zheng_ze
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
import re

__author__ = 'Kirk'

a = 'My name is 023'
r = re.match(r"\d+", a[::-1])
print(r.group()[::-1])


def find(se_lf):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', se_lf)
    return url


self = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
s = find(self)
print("Urls: ", s)
