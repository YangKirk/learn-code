# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     writte_read_file
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'Kirk'

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)
