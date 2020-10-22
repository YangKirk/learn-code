# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mao_pao
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'Kirk'


# 冒泡排序

def bubble_sort(a_rr):
    n = len(a_rr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if a_rr[j] > a_rr[j + 1]:
                a_rr[j], a_rr[j + 1] = a_rr[j + 1], a_rr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print("排序后的数组:")
for _ in range(len(arr)):
    print("%d" % arr[_])
