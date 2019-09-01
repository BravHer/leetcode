class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 0
        l = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j = j + 1
                l = l + 1
        nums[j] = nums[len(nums) - 1]

        return l

s = Solution()
t = s.removeDuplicates([1,1,1,2,4,4,5,6])
print(t)