# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_1st
   Description :
   Author :       Kirk
   date：          2020/1/14
-------------------------------------------------
   Change Activity:
                   2020/1/14:
-------------------------------------------------
"""
from typing import List

__author__ = 'Kirk'

nums = [1, 2, 2, 4]
target = 4


class Solution:
    @classmethod
    def two_sum(cls, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                break

        if j >= 0:
            return [j, i]


s = Solution()
r = s.two_sum(nums, target)
print(r)