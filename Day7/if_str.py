# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     if_str
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'Kirk'

# 测试实例一
print("测试实例一")
s_tr = "runoob.com"
print(s_tr.isalnum())  # 判断所有字符都是数字或者字母
print(s_tr.isalpha())  # 判断所有字符都是字母
print(s_tr.isdigit())  # 判断所有字符都是数字
print(s_tr.islower())  # 判断所有字符都是小写
print(s_tr.isupper())  # 判断所有字符都是大写
print(s_tr.istitle())  # 判断所有单词都是首字母大写，像标题
print(s_tr.isspace())  # 判断所有字符都是空白字符、\t、\n、\r

print("------------------------")

# 测试实例二
print("测试实例二")
st_r = "runoob"
print(st_r.isalnum())
print(st_r.isalpha())
print(st_r.isdigit())
print(st_r.islower())
print(st_r.isupper())
print(st_r.istitle())
print(st_r.isspace())
