# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        l = ListNode(0)
        d = l
        count = 0

        while p1 and p2:
            s = p1.val + p2.val + count
            count = int(s / 10)
            d.next = ListNode(s % 10)
            d = d.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            s = p1.val + count
            count = int(s / 10)
            d.next = ListNode(s % 10)
            d = d.next
            p1 = p1.next
        while p2:
            s = p2.val + count
            count = int(s / 10)
            d.next = ListNode(s % 10)
            d = d.next
            p2 = p2.next

        if count:
            d.next = ListNode(count)

        return l.next


s = Solution()
l11 = ListNode(3)
l12 = ListNode(4)
l13 = ListNode(2)
l11.next = l12
l12.next = l13

l21 = ListNode(4)
l22 = ListNode(6)
l23 = ListNode(5)
l21.next = l22
l22.next = l23

print(s.addTwoNumbers(l11,l21))
t = s.addTwoNumbers(l11,l21)
print(t.val)
print(t.next.val)
print(t.next.next.val)

