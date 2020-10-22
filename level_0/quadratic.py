# -*- coding: utf-8 -*-

import math
print('ax^2+bx+c=0')
def quadratic(a,b,c):
    for i in (a1,b1,c1):
        if not isinstance(i, (int,float)):
            raise TypeError('格式错误，请填写数字！')
    e = b*b - 4*a*c
    if e<0 or a == 0:
        raise TypeError('函数不符合解根条件')
    x1 = (-b+math.sqrt(e)) / (2*a)
    x2 = (-b-math.sqrt(e)) / (2*a)
    if x1 == x2:
        print('您的一元二次方程有且只有一个根')
        return x1
        print(quadratic(a,b,c))
    else:
        print('您的一元二次方程的两个解分别为：')
        return x1,x2
        print(quadratic(a,b,c))
a1 = input('请输入a的值:')
b1 = input('请输入b的值:')
c1 = input('请输入c的值:')
a = int(a1)
b = int(b1)
c = int(c1)
print(quadratic(a,b,c))