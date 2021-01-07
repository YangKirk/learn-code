# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      leetcode_14th
    Description:
    Author:         Kirk
    Date:           2021/1/7
-----------------------------------------
    Change Activity:
                    2021/1/7
-----------------------------------------
"""


# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
class Solution:
    @staticmethod
    def longestcommonprefix(strs: list):
        #         if not strs:
        #             return ""
        #         str0 = min(strs)
        #         str1 = max(strs)
        #         for i in range(len(str0)):
        #             if str0[i] != str1[i]:
        #                 return str0[:i]
        #         return str0
        #

        s = ""
        # zip()方法压缩打包成元组，zip(*)方法解压为列表
        for i in zip(*strs):
            print(list(i))
            print(set(i))
            # len(set()) 集合是无序不重复的，利用不重复性，判断如果长度不为1，则有两个字母
            if len(set(i)) == 1:
                s += i[0]
                print(s)
            else:
                return s


s = Solution()
print(s.longestcommonprefix(strs=["flower", "flow", "flight"]))
