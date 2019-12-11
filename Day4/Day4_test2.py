# -*- coding: utf-8 -*-
'''
# 送代字典中的键与值
dict1 = {'key1': 123, 'key2': 'asdf', 'key3': (1, 2, 3)}
# 默认是送代每一个键
for key in dict1:
    print(key, end=' ')
print()
# 通过dict.values()方法可以送代输出值
for value in dict1.values():
    print(value, end=' ')
print()
# 通过dict.items()方法可以送代输出每一对键值对
for k, v in dict1.items():
    print("{}:{}".format(k, v))

'''
'''
# 判断一个对象是可送代对象
from collections.abc import Iterable

if isinstance('abc', Iterable):
    print('1')
if isinstance([1, 2, 3], Iterable):
    print('1')
if isinstance(123, Iterable):
    print('1')
else:
    print('None')
    
'''

# 实现列表的下标位置和值一起送代，用enumerate()函数
'''
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
'''

'''
# 同时用两个变量，输出列表中的数
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''


# 用送代查找一个list中的最小值和最大值，返回一个tuple:
def findMinAndMax(X):
    for i in X:
        max = X[0]
        min = X[0]
        if i > max:
            max = i
            continue
        if i < min:
            min = i
            continue
    return max, min

li1 = [1, 2, 4,6,7,10]
print(findMinAndMax(li1))
print(type(findMinAndMax(li1)))
