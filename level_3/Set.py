# -*- coding: utf-8 -*-

# 集合set 创建需要一个列表，集合中元素输出是不重复且无序的
set1 = set([123, 789, 456, 456, 123])
print(set1)

# set 通过add(key）方法添加元素
set1.add(100)
set1.add(100)
set1.add(0)
print(set1)

# set 通过remove(key)方法删除元素
set1.remove(456)
print(set1)
print()

# set 通过 & | - 取交集，并集，差集
set2 = set([123, 100])
print(set1)
print(set2)
print('交集：{}'.format(set1 & set2))
print('并集：{}'.format(set1 | set2))
print('差集：{}'.format(set1 - set2))
print()

# 通过set 去除list中重复元素
list1 = [1, 2, 3, 4, 3, 2, 1]
se1 = set(list1)
print(se1)
