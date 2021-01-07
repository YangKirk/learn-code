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
__author__ = 'Kirk'

# 1.两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 你可以按任意顺序返回答案。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
#
# 提示：
#
# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案


num = [1, 2, 2, 4]
tar = 4


class Solution:
    @classmethod
    def two_sum(cls, nums: list, target: int):
        lens = len(nums)
        for i in range(1, lens):
            temp = nums[:i]
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                if j >= 0:
                    return [j, i]
                break


s = Solution()
r = s.two_sum(num, tar)
print(r)
