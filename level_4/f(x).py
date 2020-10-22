# -*- coding: utf-8 -*-

# 两数之和sum()函数
def sum(num1, num2):
    # 如果不是int 和float 型的参数值,就会报错
    if not (isinstance(num1, (int, float))) and isinstance(num2, (int, float)):
        raise TypeError('参数类型错误')
    return num1 + num2


print(sum(1, 2))


# 两数的商和余数
def division(num1, num2):
    if not (isinstance(num1, (int, float))) and isinstance(num2, (int, float)):
        raise TypeError('参数类型错误')
    else:
        a = num1 % num2
        b = (num1 - a) / num2
        return a, b


num1, num2 = division(9, 4)
tuple1 = division(9, 4)

print(num1, num2)
print(tuple1)


# 如果 b 是一个list或者dict，可以使用 None 作为默认值
def print_info(a, b=None):
    if b is None:
        b = []
    return a, b


print(print_info(5, ))

# 判断默认参数有没有值传入
_no_value = object()


def print_obj(a, b=_no_value):
    if b is _no_value:
        print('b没有赋值')
        return a
    else:
        return a, b


print(print_obj(10, ))  # {123: 'abc', 'cc': 12222}


# * 是只接受关键字参数,**hobby不定长关键字参数，此时hobby是一个字典，*hobby是可变参数，此时hobby是一个元组
# def user_info(name, age, sex='男', *hobby):
def user_info(name, *, age, sex='男', **hobby):
    print('昵称：{}'.format(name), end='')
    print('年龄：{}'.format(age), end='')
    print('性别：{}'.format(sex), end='')
    print('爱好：{}'.format(hobby))
    return;


# user_info('VV', '22', '女', ('吃饭', '睡觉', '看剧'))
user_info('Kirk', age=23, hobby=('吃饭', '睡觉', '打游戏'))


# 函数传值整型浮点数字符串元组不能更改值，列表和字典可以更改
def change_num(b):
    print('函数中一开始b的值为：{}'.format(b))
    b = 1000
    print('函数中b赋值后的值为：{}'.format(b))


b = 1
change_num(b)
print('最后输出b的值为：{}'.format(b))


# 列表的值可以改变
def change_list(b):
    print('函数中一开始b的值为：{}'.format(b))
    b.insert(0, 123)
    b.append(110)
    b.pop(1)
    print('函数中b赋值后的值为：{}'.format(b))


b = ['key1', '1123', 'key2', 'abc', [1, 2, 3, ], 'zzzz']
change_list(b)
print('最后输出b的值为：{}'.format(b))


# 字典的值可以改变
def change_dict(b):
    print('函数中一开始b的值为：{}'.format(b))
    del b['key1']
    b.clear()
    b[(1, 2, 3)] = 'love'
    print('函数中b赋值后的值为：{}'.format(b))


b = {'key1': '1123', 'key2': 'abc', 'key3': [1, 2, 3]}
change_dict(b)
print('最后输出b的值为：{}'.format(b))
