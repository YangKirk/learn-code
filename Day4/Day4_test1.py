# -*- coding: utf-8 -*-
# 创建一个函数trim（），移除字符串首尾的空格，不使用strip（）方法
'''
def trim(s: str):
    for i in s[:]:
        if i == ' ':
            continue
        else:
            print(i, end='')


trim('     asddsaf        ')
'''
# 使用strip()函数方法
s = '   asdf   '
print(s.strip(' '))

