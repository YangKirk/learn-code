# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     import
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
import calendar
import datetime
import doctest
import random
import re
import sys
import os
import glob
import time
import unittest
import zlib
from timeit import Timer

import math

from numpy import average


__author__ = 'Kirk'

# os
s = os.getcwd()  # 获取返回当前目录
# os.system('mkdir today')  # 新建文件夹today
# print(s)

# help()&dir()
# print(help(os))
# print(dir(os))

# glob
r = glob.glob('*.py')
# print(r)

# sys
if r == s:
    sys.exit()  # 终止程序
# print(s, r)

# re
f = re.findall(r'\bf[a-z]]*', r'which foot or hand fell fastest')
b = re.sub(r'(\b[a-z]]+)', r'\1', r'cat in the the hat')
# 'tea for too'.replace('too', 'two')  # 简单的功能优先考虑字符串方法
# print(f, '\n', b)

# math
p = math.cos(math.pi / 4)
# print(p)
lo = math.log(1024, 2)
# print(lo)


# random
xr = random.choice(['apple', 'pear', 'banana'])
# print(xr)
xs = random.sample(range(100), 10)  # sample 不更换采样
# print(xs)
xf = random.random()  # random float
# print(xf)
xd = random.randrange(6)  # 从范围()中随机整数,例如范围6
# print(xd)

# datetime
today = datetime.date.today()  # 今天
yesterday = today - datetime.timedelta(days=1)
last_month = today.month - 1 if today.month - 1 else 12
time_stamp = time.time()  # 当前时间戳
datetime_time_stamp = datetime.datetime.fromtimestamp(time_stamp)  # 时间戳转datetime
time_stamp_datetime = int(time.mktime(today.timetuple()))
datetime_str = today.strftime("%Y-%m-%d")  # datetime转字符串
str_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d")  # 字符串转datetime
sc_time = datetime_time_stamp + datetime.timedelta(hours=8)  # 补时差
# print(today)
# print(yesterday)
# print(today.month-1)  # month要求return 1-12的整数，如果差为0，则返回12
# print(last_month)
# print(time_stamp)
# print(datetime_time_stamp)
# print(time_stamp_datetime)
# print(datetime_str)
# print(str_datetime)
# print(sc_time)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = datetime.date(1997, 6, 25)
age = today - birthday  # 计算距今多少天
days = age.days
# print(days)

# zlib
s = b'witch which has which witches wrist watch'
# print(len(s))
t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))


# timeit.Timer 测试代码性能
a1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
a2 = Timer('a,b = b,a', 'a=1;b=2').timeit()
# print(a1, '\n', a2)

# doctest 模块测试
re1 = doctest.testmod()  # 自动验证嵌入测试


# print(p)

# unittest 类的测试
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


# re2 = unittest.main()
# print(re2)


# calendar 日历模块
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))

# 显示日历
# print(calendar.month(yy, mm))
# 计算每个月天数
monthRange = calendar.monthrange(2016, 9)
print(monthRange)
