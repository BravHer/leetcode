class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = []           #������
        #��ÿ�������еĵ�һ��Ԫ�ؼ�����У���ά������С�ѵ���ʽ
        for ln in lists:
            if ln:
                heap.append((ln.val, ln))  #���Ԫ��ֵ������
        
        dummy = ListNode(0) #�������ս��
        cur = dummy         #���ϲ�������
        heapq.heapify(heap)  #ά������С����ʽ
        while heap:
            valu, ln_index = heapq.heappop(heap)  #������Сֵ����Ӧ������ֵ
            cur.next = ln_index
            cur = cur.next
            #ȡ����Ԫ��ԭ��������list�е���һ��Ԫ�ط������
            if ln_index.next:
                heapq.heappush(heap, (ln_index.next.val, ln_index.next))
        return dummy.next
