class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2

            if nums[mid] == target:
                return mid

            if nums[left] >= target:
                if target < nums[mid] and nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target and nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

