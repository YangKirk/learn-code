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
