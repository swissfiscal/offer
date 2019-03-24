#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created on 2019/3/12
 @author: luomashuzi
 desc:

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
输出: true
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1:return l2
        # if not l2:return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        # 头结点，前一个节点
        dummy = pre = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 or l2
        return dummy.next
if __name__ == '__main__':
    # l1=[1,2,4]
    # l2=[1,3,4]
    # for (i1, i2) in zip(l1,l2):
    #     print(i1,i2)

    a=Solution()
    print(a.mergeTwoLists([1,2,4],[1,3,4]))