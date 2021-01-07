# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      leetcode_21st
    Description:
    Author:         Kirk
    Date:           2021/1/7
-----------------------------------------
    Change Activity:
                    2021/1/7
-----------------------------------------
"""


# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_list(self, l1, l2):
        if not l1:
            return l2  # 终止条件，直到两个链表都空
        if not l2:
            return l1

        if l1.val <= l2.val:  # 递归调用
            l1.next = self.merge_two_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list(l1, l2.next)
            return l2
