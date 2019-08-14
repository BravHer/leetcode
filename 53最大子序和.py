'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray

'''
'''class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxs = nums[0]
        maxsub = 0

        for i in range(0, len(nums)):
            maxsub += nums[i]
            maxs = max(maxsub, maxs)

            if maxsub < 0:
                maxsub = 0
        return maxs
'''
# 动态规划
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1):
            submax = max(nums[i] + nums[i + 1], nums[i + 1])
            nums[i + 1] = submax

        return max(nums)
