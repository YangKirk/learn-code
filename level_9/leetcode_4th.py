# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_4th
   Description :  
   Author :       kirk
   date：          2021/9/3
-------------------------------------------------
   Change Activity:
                   2021/9/3
-------------------------------------------------
"""
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

class Solution:
    @staticmethod
    def find_median_sorted_arrays(nums1: list, nums2: list):
        for _ in nums2:
            nums1.append(_)
        nums1.sort()
        if len(nums1) % 2 == 0:
            a = len(nums1) // 2
            return float((nums1[a] + nums1[a - 1]) / 2)
        else:
            a = int(len(nums1) / 2)
            return nums1[a]
