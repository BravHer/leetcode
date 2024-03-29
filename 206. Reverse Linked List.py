'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        newhead = stack[-1]
        p = newhead
        stack.pop()
        while stack:
            p.next = stack.pop()
            p = p.next

        p.next = None
        return newhead
