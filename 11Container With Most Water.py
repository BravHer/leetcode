class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, max = 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                tmp = height[left] * (right - left)
                left = left + 1
            else:
                tmp = height[right] * (right - left)
                right = right - 1
            if tmp > max:
                max = tmp

        return max

