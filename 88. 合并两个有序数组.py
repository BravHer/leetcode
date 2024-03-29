'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m = m - 1
        n = n - 1
        while m >= 0 and n >=0:
            if nums1[m] < nums2[n]:
                nums1[m + n + 1] = nums2[n]
                n = n - 1
            else:
                nums1[m + n + 1] = nums1[m]
                m = m - 1
        while n >= 0:
            nums1[n] = nums2[n]
            n = n - 1




s = Solution()
print(s.merge([1,2,3],0, [2,5,6], 3))


s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))