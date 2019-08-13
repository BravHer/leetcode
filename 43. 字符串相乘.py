'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
'''

'''class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str2int(num1) * self.str2int(num2))

    def str2int(self, str):
        num = 0
        for i in range(0, len(str)):
            num = num + (10 ** (len(str) - 1 - i)) * int(str[i])
        return num


s = Solution()
print(s.multiply('2', '3'))

s = Solution()
print(s.multiply('123', '456'))


