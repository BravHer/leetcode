class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = []           #创建堆
        #将每个链表中的第一个元素加入对中，并维护成最小堆的形式
        for ln in lists:
            if ln:
                heap.append((ln.val, ln))  #添加元素值与索引
        
        dummy = ListNode(0) #返回最终结果
        cur = dummy         #不断补充链表
        heapq.heapify(heap)  #维护成最小堆形式
        while heap:
            valu, ln_index = heapq.heappop(heap)  #弹出最小值和相应的索引值
            cur.next = ln_index
            cur = cur.next
            #取出该元素原先所处的list中的下一个元素放入堆中
            if ln_index.next:
                heapq.heappush(heap, (ln_index.next.val, ln_index.next))
        return dummy.next
