class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        # print(nums)
        val = []
        i = 0
        while i < len(nums) - 2:
           left, right =  i + 1, len(nums) - 1

           while left < right:
               result = nums[i] + nums[left] + nums[right]
               res = []
               if result < 0:
                   left = left + 1
               elif result > 0:
                   right = right - 1
               else:
                   res.append(nums[i])
                   res.append(nums[left])
                   res.append(nums[right])

                   val.append([nums[i], nums[left], nums[right]])
                   left = left + 1
                   right = right - 1
                   while left < right and nums[left] == nums[left - 1]:
                       left = left + 1
                   while left < right and nums[right] == nums[right + 1]:
                       right = right - 1

           while i < len(nums) - 2 and nums[i] == nums[i + 1]:
               i = i + 1
           i = i + 1
        return  val

s =Solution()
t = s.threeSum([-1,0,1,2,-1,-4])
print(t)

