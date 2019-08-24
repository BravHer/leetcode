'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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
        l = ListNode(0)
        sum = 0
        tmp = l
        while True:
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next
            tmp.val = sum % 10
            sum = sum // 10
            # 结束的条件 两个链表同时为空 并且没有进位（5 + 5 = 10）
            if not l1 and not l2 and sum == 0:
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
        return l

'''
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
'''

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

