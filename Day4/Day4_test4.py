# -*- coding: utf-8 -*-

# 生成器generator与列表生成式之前区别()与[]
g = (x * x for x in range(5))
for n in g:
    print(n, end='')
print()
