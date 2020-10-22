# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_buyu
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'Kirk'

"""
题目：
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们台伙至少捕了多少条鱼?
"""


# 方法一
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


if __name__ == '__main__':
    main()

# 方法二
n = 1
person1 = (n - 1) / 5
person2 = (person1 * 4 - 1) / 5
person3 = (person2 * 4 - 1) / 5
person4 = (person3 * 4 - 1) / 5
person5 = (person4 * 4 - 1) / 5

while True:

    if int(person1) == person1 and int(person2) == person2 and int(person3) == person3 and int(
            person4) == person4 and int(person5) == person5:
        break

    else:
        n += 1
        person1 = (n - 1) / 5
        person2 = (person1 * 4 - 1) / 5
        person3 = (person2 * 4 - 1) / 5
        person4 = (person3 * 4 - 1) / 5
        person5 = (person4 * 4 - 1) / 5

print('There are %d fish in total.' % n)
