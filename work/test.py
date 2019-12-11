
def sum(num1,num2):
    if not(isinstance (num1,(int,float)) and (nume2,(int,float))):
        raise TypeError('参数类型错误')
        return num1+num2

print(sum(1,2))

def guess_num():
    import random
    guess_n = random.randint(1, 100)
    while True:
        num = int(input("请输入整数："))
        if num > guess_n:
            print('数字大了。')
        elif num < guess_n:
            print('数字小了。')
        else:
            print('猜对了！')
            break
guess_num()