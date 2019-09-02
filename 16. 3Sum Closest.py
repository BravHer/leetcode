class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        sum = 999999
        nums.sort()
        for i in range(0, len(nums)):
            # for j in range(i + 1, len(nums)):
            #     for k in range(j + 1, len(nums)):
            #         if abs(target - nums[i] - nums[j] - nums[k]) < abs(target - sum):
            #             sum = nums[i] + nums[j] + nums[k]
            # j, k = i + 1

            left = i + 1
            right = len(nums) - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                # print(result)
                if abs(target - result) < abs(target - sum):
                    sum = result

                if result < target:
                    left = left + 1
                elif target < result:
                    right = right - 1
                elif target == result:
                    return target
        return sum

s = Solution()
t = s.threeSumClosest([-1,2,1,-4], 1)
print(t)