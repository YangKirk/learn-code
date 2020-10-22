'''
1.  # 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21...
a = 1
b = 1
for i in range(1, 10):
    print("{},{}".format(a, b),end='')
    if (i % 3) == 0:
        print()
    a = a +b
    b =a+b
'''
'''
2.  # 判断101-200之间有多少个素数，并输出所有素数
sum1 = 0
for i in range(101, 201):
    for j in range(1, i+1):
        if j == 1 or j == i:
            continue
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        sum1 += 1
print()
print("在101-200之间总共有{}个素数".format(sum1))
'''
'''
3. # 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100, 1000):
    sum1 = 0
    for j in str(i):
        sum1 += int(j) ** 3
    if sum1 == i:
        print(i, end=' ')

print()
'''
'''
4.  # 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
S = int(input("请输入学生的成绩："))
if S >= 90:
    print("该学生成绩为A！")
elif S >= 60:
    print("该学生成绩为B！")
else:
    print("该学生成绩为C！")

'''
'''
5  # 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
alpha = 0
space = 0
digit = 0
other = 0
s = input("请输入一行字符：")
for i in s[:]:
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1
print("字符串中的英文字母个数为：{}\n字符串中的空格字符个数为：{}\n字符串中的数字字符个数为：{}\n字符串中的其他字符个数为：{}".format(alpha, space, digit, other))
'''
'''
6.  # 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a = input("请输入第一个数字：")
n = int(input("请输入第二个数字："))
s = 0
print("输出S=", end='')
for i in range(1, n + 1):
    if i != n:
        print("{}+".format(a * i), end='')

    else:
        print("{}".format(a * i), end='')
    s += int(a * i)
print("\n计算以上式子求和结果为：{}".format(s))
'''
'''
7.  # 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

m = 1000
for i in range(2, m + 1):
    k = []
    s = i
    for j in range(1, i):
        if i % j == 0:
            s -= j
            k.append(j)
    if s == 0:
        print("完数：%d 因数包括：" % i, end=' ')
        for a in range(0, len(k)):
            print("%d" % k[a], end=' ')
        print('\n')
'''
