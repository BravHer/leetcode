'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if (n+m) % 2 == 0:
            flag = True
        else:
            flag = False
        middle_index = (n + m) / 2 + 1
        nums1_index, nums2_index = 0, 0
        l3 = []
        while nums1_index < n and nums2_index < m:
            if nums1[nums1_index] > nums2[nums2_index]:
                l3.append(nums2[nums2_index])
                nums2_index += 1
            else:
                l3.append(nums1[nums1_index])
                nums1_index += 1
            if len(l3) == middle_index:
                break
        while nums1_index < n and nums2_index == m:
            if len(l3) == middle_index:
                break
            l3.append(nums1[nums1_index])
            nums1_index += 1
            if len(l3) == middle_index:
                break
        while nums2_index < m and nums1_index == n:
            if len(l3) == middle_index:
                break
            l3.append(nums2[nums2_index])
            nums2_index += 1

        if flag:
            middle_value = (l3[len(l3)-2] + l3[len(l3)-1])/2.0
        else:
            middle_value = l3[len(l3)-1]
        return middle_value

s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))