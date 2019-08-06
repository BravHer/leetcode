
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kmaxs = [float('-inf')]*k    # 存储前k大个值
        for i in range(len(nums)):
            j = 0
            while j<k:
                if nums[i]> kmaxs[j]:
                    kmaxs[j+1:] = kmaxs[j:k-1]   #有元素要改变时，先将待改变的当前元素值及之后元素依次向后赋值
                    kmaxs[j] = nums[i]           # 然后修改要改变的当前元素
                    break
                else:
                    j +=1
        return kmaxs[k-1]
