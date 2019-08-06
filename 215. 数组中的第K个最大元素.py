
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kmaxs = [float('-inf')]*k    # �洢ǰk���ֵ
        for i in range(len(nums)):
            j = 0
            while j<k:
                if nums[i]> kmaxs[j]:
                    kmaxs[j+1:] = kmaxs[j:k-1]   #��Ԫ��Ҫ�ı�ʱ���Ƚ����ı�ĵ�ǰԪ��ֵ��֮��Ԫ���������ֵ
                    kmaxs[j] = nums[i]           # Ȼ���޸�Ҫ�ı�ĵ�ǰԪ��
                    break
                else:
                    j +=1
        return kmaxs[k-1]
