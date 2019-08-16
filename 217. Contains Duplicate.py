'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''
# 字典的方法
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if n not in d.keys():
                d[n] = 1
            else:
                return True
        return False
'''
# set 集合
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 
'''

s = Solution()
print(s.containsDuplicate([1,2,3,1]))

s = Solution()
print(s.containsDuplicate([1,2,3,4,6,7,88]))

s = Solution()
print(s.containsDuplicate([1,2,3,44,55,66,3,1]))