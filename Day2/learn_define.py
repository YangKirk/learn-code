"""
0. 封装函数，给所有传入的字符串加上你的名字：
 例如：定义函数 i_talk("你好")
 输出：包子说：你好
"""


def say_hi(s):
    name = '包子：'
    print("%s%s" % (name, s))


"""
2. 定义函数，计算两数之和

"""


def sum_num(n1, n2):
    print(n1 + n2)


"""
3. 定义函数，传入一个整数，返回0到这个数的正整数之和

"""


def sum_arg(arg: int):
    n = 0
    for i in range(1, arg + 1):
        n += i
    print(n)


"""
定义函数：分数检查
分数范围：-1-100整数
89及以上 优秀
69到90 良好
59到70 中等
59以下 不及格
"""


def score(num: int):
    if num not in range(0, 101):
        print("请输入0-100的分数")
    elif num >= 90:
        print('优秀')
    elif num >= 80:
        print('成绩良好')
    elif num >= 70:
        print('成绩中等')
    elif num >= 60:
        print('成绩及格')
    else:
        print('抱歉，未及格。')


"""
4. 定义函数：传入一个一个9以内的正整数。输出数字组成的如下图像
        1 
       2 2 
      3 3 3 
     4 4 4 4 
    5 5 5 5 5 
   6 6 6 6 6 6 
  7 7 7 7 7 7 7 
.................
"""


def pyramid(num: int):
    for i in range(1, num + 1):  # 第一层级：1 到 num
        print(" " * (num - i), end='')  # 计算需要空多少个空格
        for j in range(i, 0, -1):  # 第二层级：
            print(i, end=' ')  # 输出一个数则空一格
        print()  # 第二层级输出完毕则换行


"""
定义函数：生成一个随机整数。猜测数字大小

"""


def guess_num():
    import random  # 引入随机数库
    guess_n = random.randint(1, 100)  # 生成1到100的随机整数
    while True:  # 死循环，会一直执行，直到触发break退出条件
        num = int(input("请输入整数："))  # 输入的整数
        if num > guess_n:
            print('数字大了。')
        elif num < guess_n:
            print('数字小了。')
        else:
            print('猜对了！')
            break  # 触发退出条件
