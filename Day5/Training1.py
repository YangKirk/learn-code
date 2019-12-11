'''
1.# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=k) and (i !=j) and (j!=k):
                print(i,j,k)
'''

'''
2.# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

I = int(input("请输入当月利润金额（万元）："))
if I <= 10:
    print("应发奖金总数为：{}".format(I * 0.1))
elif I < 20:
    print("应发奖金总数为：{}".format((I - 10) * 0.075 + 10 * 0.1))
elif I < 40:
    print("应发奖金总数为：{}".format((I - 20) * 0.05 + 10 * 0.075 + 10 * 0.1))
elif I < 60:
    print("应发奖金总数为：{}".format((I - 40) * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1))
elif I < 100:
    print("应发奖金总数为：{}".format((I - 60) * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1))
else:
    print("应发奖金总数为：{}".format((I - 100) * 0.01 + 40 * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1))

'''
'''
3.# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# x + 100 = m**2    x+100+168 = n**2
# n**2 - m**2 = 168 => (n+m)(n-m) = 168
# n+m = i , n-m = j => 2n = i+j => i+j /2 = n  i-j /2 = m
for i in range(1, 169):
    for j in range(1, 168):
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 and i * j == 168:
            m = (i - j) / 2
            n = (i + j) * 2
            x1 = m ** 2 - 100
            print(x1)
   
'''
'''
4.# 输入某年某月某日，判断这一天是这一年的第几天？
year = int(input("请输入年份日期\n年："))
mon = int(input("月："))
day = int(input("日："))

sum1 = 0
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < day <= 31:
    sum1 += day
if 0 < mon <= 12:
    sum1 += months[mon - 1]
else:
    print("月份输入错误！")
if (year % 400 ==0) or (year % 4 == 0) and (year % 100 != 0):
    sum1 += 1

print("输入的日期是{}的第{}天！".format(year, sum1))
'''
'''
5.# 输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))
z = int(input("请输入第三个数："))
l = []
for i in (x, y, z):
    l.append(i)
l.sort()
print(l)

'''

'''
6.# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
def fib(n):
    a, b = 1, 1
    l1 = []
    for i in range(n - 1):
        a, b = b, a + b
        l1.append(a)
    return l1


print(fib(int(input("请输入一个数，将输出黄金分割数列："))))
'''
'''
7.# 将一个列表的数据复制到另一个列表中
# 1
l1 = [1,2,3,4,5]
l2 = []
l2 = l1.copy()
print(l2)

# 2
l1 = [1,2,3]
l2 = l1[:]
print(l2)

# 3
l1 = [1,2,3]
l2 = []
for i in l1[:]:
    l2.append(i)
print(l2)

# 4
l1 = [1,2,3]
l2 = []
l2.extend(l1)
print(l2)
'''
'''
8.  # 输出 9*9 乘法口诀表。

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("{}*{}={}\t".format(i, j, i * j),end='')
    print()
'''
'''
9.# 暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。

import time

dict1 = {'a': 2, 'b': 13}
for key, value in dict1.items():
    print("{}={}".format(key, value))
    time.sleep(1)
'''
'''
10.# 暂停三秒输出，并格式化当前时间。

import time
# 第一次输出
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
# 暂停三秒，再次输出
time.sleep(3)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

'''
