"""
1. 打印 hello world
"""
print("hello world")

"""
2. 求 22除以10的余数
"""
print(22 % 10)

"""
3. 打印 1~9 之间的整数
1 2 3 ... 9
"""
for i in range(1, 10):
    print(i, end=" ")
print()

"""
4. 打印10到1之间的数
10 9 ... 1
"""
for i in range(10, 0, -1):
    print(i, end=" ")
print()

"""
5. 打印1~20之间的正整数之和
1+2+3+..+20
"""
n_sum = sum(range(1, 21))
print(n_sum)

""" 
6. 用"for循环"打印一个像下面一样的三角形
    *
   **
  ***
 ****
*****
"""
for i in range(5):
    print((4 - i) * " ", end="")
    print((i + 1) * "*")

"""
7. 给定一个列表[1,2,3,4,5,6]，去掉列表里所有的偶数。
[1, 3, 5]
"""
li = [1, 2, 3, 4, 5, 6]
# 1
for item in li[:]:
    if item % 2 == 0:
        li.remove(item)
# 2
li = [x for x in li if x % 2 != 0]
print(li)
"""
8. 写一个函数，传入字符串，把所有小写字母改为大写，"-"改为"_"
例传入"abc-abc-abc"，返回"ABC_ABC_ABC"
"""
str1 = "abc-abc-abc"
new_str = ""
for s in str1:
    if s.isalpha():
        new_str += s.upper()
    if s == "-":
        new_str += "_"
print(new_str)

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
        print(i, end=" ")
print()

"""
10. 打印出100以内能同时被3和5整除的正整数
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()

"""
11. 打印所有水仙花数 
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
（例如：1^3 + 5^3+ 3^3 = 153）
"""

for i in range(100, 1000):
    total = 0
    for char in str(i):
        total += int(char) ** 3
    if total == i:
        print(i, end=" ")
print()

"""
12. 设计一个函数，接收3个数，并按大小顺序输出
"""


def foo(num1, num2, num3):
    for num in {num1, num2, num3}:
        print(num, end=" ")
    print()


"""
13. s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
"""
s = "ajldjlajfdljfddd"
res = ""
for c in s:
    if c not in res:
        res += c
res = "".join(sorted(res))
print(res)

"""
14. 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]
"""
li1 = [1, 5, 7, 9]
li2 = [2, 2, 6, 8]
li1 += li2
li1.sort()
print(li1)
