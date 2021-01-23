# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cook_book_1
   Description :
   Author :       Kirk
   date：          2020/1/8
-------------------------------------------------
   Change Activity:
                   2020/1/8:
-------------------------------------------------
"""

# 问题1：现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# 解压需要N个元素的N = N个变量的N，也就是变量数量要一致
"""
# 解压字符串
s = 'Hello'
a, b, c, d, e = s
print(a)
"""

"""
# 解压列表或元组其中一部分，可用任意变量占位
data = ['ACME', 50, 91.1, (2020, 1, 8)]
_, shares, price, _ = data
print(shares, price)
"""

# 问题2：现在有一个包含 M 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# 此时 M>N
"""
# 星号表达式函数
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


data = drop_first_last(['ACME', 50, 25, 44, 'xxx',
                       91.1, (2020, 1, 8)])
print(data, type(data))
"""

"""
# 星号表达式直接解压
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)  # 星号表达式返回的数据永远是列表类型
"""
"""
# 星号表达式解压可变长元组列表
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
"""

"""
# _丢弃处理
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)
"""

# 问题3：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
