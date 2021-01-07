# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      leetcode_9th
    Description:
    Author:         Kirk
    Date:           2021/1/7
-----------------------------------------
    Change Activity:
                    2021/1/7
-----------------------------------------
"""


# 9. 回文数
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？

# 转为字符串解决
class Solution:
    @staticmethod
    def is_palindrome(x: int):
        a = str(x)
        if a[::-1] == a[:]:
            return True
        else:
            return False
        # return str(x) == str(x)[::-1]


# s = Solution()
# print(s.is_palindrome(-121))

# 不转为字符串解决
class Solution2:
    @staticmethod
    def is_palindrome_2(x: int):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        ans = 0
        while x > ans:
            ans = ans * 10 + x % 10
            x //= 10
        return x == ans or x == (ans // 10)

# s = Solution2()
# print(s.is_palindrome_2(12321))
