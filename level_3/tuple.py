# 以每次加3的方式按序输出1-10
for i in range(1, 10, 3):
    print(i)

# 依次输出字典里每个键
dict1 = {'k1': 'abc', 123: 'ccc', ('1', '2', '3'): 'xxxx'}
for i in dict1:
    print(i)

# 逐字输出字符串
for letter in 'asdf两点睡':
    print(letter)

# 输出20以内的质数和合数
for num in range(1, 20):
    for i in range(2, num):
        if num % i == 0:
            print('%d 这是一个合数' % num)
            break
    else:
        print('%d 这是一个质数' % num)

# 输出9*9乘法表
for i in range(1, 10):
    print('{}'.format((10 - i) * ' ' * (9 // 2)), end='')
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(i, j, i * j), end='')
    print()

# 判断是否是闰年
year = int(input("请输入一个年份：\n"))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))
