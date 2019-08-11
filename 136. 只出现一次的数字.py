'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        i = 0
        while(i <= len(nums) - 2):

            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i = i + 2
        return nums[i]

'''
# 键值对key，value
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = collections.Counter(nums)
        for key,value in x.items():
            if value < 2:
                return key
'''

'''
# 异或运算
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sn = 0
        for nu in nums:
            sn ^= nu
        return sn

'''


s = Solution()
print(s.singleNumber([2,2,1,3,3]))

s = Solution()
print(s.singleNumber([2,2,1]))

s = Solution()
print(s.singleNumber([2,2,1,1,3]))