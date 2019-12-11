"""
1. 打印 hello world
"""  # 打印 hello world
print('hello world')

"""
2. 求 22除以10的余数
"""  # 求 22 除以 10 的余数
a = 22
b = 10
c = a % b
print(c)

"""
3. 打印 1~9 之间的整数
1 2 3 ... 9
"""
for i in range(1, 10):  # range(开始，结束)包含前面，不包含后面
    print(i, end=' ')  # end=''换行
print()
# a = 1
# while a < 10:
# print(a)
# a += 1

"""
4. 打印10到1之间的数
10 9 ... 1
"""

a = 10
while a >= 1:
    print(a, end=' ')
    a -= 1
print()

"""
5. 打印1~20之间的正整数之和
1+2+3+..+20
"""

a = 1
i = 0
while a < 21:
    i = i + a
    a += 1
print(i)
""" 
6. 用"for循环"打印一个像下面一样的三角形
    *
   **
  ***
 ****
*****
"""
i = ' '
a = '*'
f = 1

for f in range(1, 6):
    for n in range(5 - f):
        print(i, end='')
        n -= 1
    print(a * f)
    f += 1

"""
7. 给定一个列表[1,2,3,4,5,6]，去掉列表里所有的偶数。
[1, 3, 5]
"""
li = [1, 2, 3, 4, 5, 6]
for item in li[:]:  # 这个[:]是针对列表的切片，保证删除一个元素后还是能取到每一个元素
    if item % 2 == 0:
        li.remove(item)
print(li)

"""
8. 写一个函数，传入字符串，把所有小写字母改为大写，"-"改为"_"
例传入"abc-abc-abc"，返回"ABC_ABC_ABC"
"""


# 方法一 用判断条件和循环嵌套来改写字符串
# stl = 'abc-abc-abc'
# stl_n = ''
# for i in stl:
#     if i.isalpha():
#         stl_n += i.upper()
#     if i == '-':
#         stl_n += '_'
# print(stl_n)

# 方法二 用replace() 函数来替换

def replay(st: str):
    st = st.upper()
    st = st.replace("-", "_")
    print(st)


stl = 'abc-abc-abc'
replay(stl)

"""
9. 打印出 1~100之间的质数(素数)
质数：只能被1和本身整除的数
2 3 5 7 11 ... 89 97
"""

for i in range(2, 101):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            continue
        if i % j == 0:
            break
    else:
        print(i, end='')

print()

"""
10. 打印出100以内能同时被3和5整除的正整数
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
        i += 1
print()
"""
11. 打印所有水仙花数 
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
（例如：1^3 + 5^3+ 3^3 = 153）
"""
# 1
for i in range(100, 1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i, end=' ')
print()
# 2

for i in range(100, 1000):
    sum1 = 0
    for j in str(i):
        sum1 += int(j) ** 3
    if sum1 == i:
        print(i, end=' ')

print()
"""
12. 设计一个函数，接收3个数，并按大小顺序输出
"""


def pnt(x, y, z):
    for num in {x, y, z}:
        print(num, end=" ")
    print()


pnt(3, 7, 5)

"""
13. s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
"""
# print(ord('a')) 输出 ”a“字符的ASCII码
s = "ajldjlajfdljfddd"
s_new = ""
for i in s:
    if i not in s_new:
        s_new += i
s_new = "".join(sorted(s_new))
print(s_new)
"""
14. 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]
"""
# 1
li1 = [1, 5, 7, 9]
li2 = [2, 2, 6, 8]
li3 = li1 + li2
li3.sort()
print(li3)
'''
# 2
for i in li2[:]:
    li1.append(i)
li1.sort()
print(li1)
'''
'''
# 3
li1.extend(li2)
print(li1)
li1.sort()
print(li1)
'''