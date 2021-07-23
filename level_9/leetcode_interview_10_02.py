# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_interview_10_02
   Description :  
   Author :       kirk
   date：          2021/7/23
-------------------------------------------------
   Change Activity:
                   2021/7/23
-------------------------------------------------
"""
import collections

"""
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

"""


class Solution:
    @staticmethod
    def group_anagrams(strs: list):
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())


if __name__ == '__main__':
    print(Solution.group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
