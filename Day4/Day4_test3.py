# -*- coding: utf-8 -*-

# list()方法生成列表
L1 = list(range(1, 11))
print(L1)

# for 循环生成表达式[1*1,2*2..., 10*10]列表
L2 = []
for x in range(1, 11):
    L2.append(x * x)
print(L2)
# 用列表生成式代替循环生成上面的列表
L3 = [x * x for x in range(1, 11)]
print(L3)

# 用两个for循环的列表生成式生成两个字符串的全排列方法列表
L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

# 也可以用两个变量来用字典生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
L5 = [k + '=' + v for k, v in d.items()]
print(L5)

# 把list 中所有字符串变小写，同理也可以变大写
l = ['Hello', 'World', 'IBM', 'Apple']
L6 = [s.lower() for s in l] # 把列表中的所有字符串变小写
print(L6)
L7 = [s.upper() for s in L6] # 把列表中的所有字符串变大写
print(L7)

# 列表生成式 [] 生成带条件判断的列表
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
