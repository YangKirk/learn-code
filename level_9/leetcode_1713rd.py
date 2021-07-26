# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_1713rd
   Description :  
   Author :       kirk
   date：          2021/7/26
-------------------------------------------------
   Change Activity:
                   2021/7/26
-------------------------------------------------
"""
import bisect

"""
给你一个数组target，包含若干 互不相同的整数，以及另一个整数数组arr，arr可能 包含重复元素。

每一次操作中，你可以在 arr的任意位置插入任一整数。比方说，如果arr = [1,4,1,2]，那么你可以在中间添加 3得到[1,4,3,1,2]。你可以在数组最开始或最后面添加整数。

请你返回 最少操作次数，使得target成为arr的一个子序列。

一个数组的 子序列指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4]是[4,2,3,7,2,1,4]的子序列（加粗元素），但[2,4,2]不是子序列。



示例 1：

输入：target = [5,1,3], arr = [9,4,2,3,4]
输出：2
解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。
示例 2：

输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
输出：3
"""


class Solution:
    @staticmethod
    def min_operations(target: list, arr: list):
        # 分析:
        # 本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少)
        # 根据target中互不相同，我们知道每个数字对应的坐标唯一
        # 于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列

        # 数字对应坐标
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300.最长上升子序列
        stack = []
        for num in arr:
            # 只有在target的数字才可能属于公共子序列
            if num in idx_dict:
                # 转换坐标
                idx = idx_dict[num]
                # 该坐标在当前栈中的位置
                i = bisect.bisect_left(stack, idx)
                # 如果在最后要加入元素，否则要修改该位置的元素
                # 跟一般的讲，i代表了目前这个idx在stack中的大小位置，
                # 在前面出现还比idx大的stack中的元素是无法和idx构成最长上升子序列的。
                # i左边的数比idx小，可以和idx构成上升子序列，(idx构成的长度就是i+1)
                # idx比i的值小，将i替换后可以方便后面构成更优的子序列(越小后面能加入的数越多)
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        # 最终stack的长度就构成了最长上升子序列的长度，用减法即可得到本题答案
        print(len(target) - len(stack))
        return len(target) - len(stack)


if __name__ == '__main__':
    Solution.min_operations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1])
