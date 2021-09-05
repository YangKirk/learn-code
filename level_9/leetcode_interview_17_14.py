# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_interview_17_14
   Description :  
   Author :       kirk
   date：          2021/9/3
-------------------------------------------------
   Change Activity:
                   2021/9/3
-------------------------------------------------
"""
"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))


"""


class Solution:
    def small_e_stk(self, arr: list, k: int):
        arr.sort()
        return arr[:k]
