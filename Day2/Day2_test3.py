def sss(n: int):
    for i in range(1, n + 1):
        if n < 10:
            print(" " * (n - i), end="")
        elif n < 100 and n >= 10:
            print(" " * (n - i) * len(str(n)), end="")
        else:
            print(" %d 不支持输出！请重新输入小于100的整数!" % n)
            break
        for j in range(1, i + 1):
            if n < 10:
                print(i, "", end='')
            else:
                if i < 10:
                    print(i, " " * len(str(n)), end='')
                else:
                    print(i, " ", end='')
        print()

sss(int(input("请输入一个100以内的整数：\n")))
