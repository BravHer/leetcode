'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42

'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        result = ''
        if not s:
            return 0

        p = 1
        if s[0]== '-':
            result = result + '-'
            for j in range(1, len(s)):
                if s[j] == '0' and p ==1:    ####处理很多-00000000000的问题
                    continue
                else: p = 0
                if not (s[j]  >= '0' and s[j]  <= '9'):
                    break
                result = result + s[j]

            if result == '-':
                return 0
            if int(result) < -2**31:
                return -2**31

            return int(result)

        if s[0] == '+' or (s[0] >= '0' and s[0] <= '9'):
            if s[0] >= '0' and s[0] <= '9':
                result = result + s[0]

            for j in range(1, len(s)):
                if not (s[j] >= '0' and s[j] <= '9'):
                    break
                result = result + s[j]

            if result == '':
                return 0
            if int(result) > 2**31 -1:
                return  2**31 - 1

            return int(result)
        return 0


s =Solution()
print(s.myAtoi("-91283472332"))

s =Solution()
print(s.myAtoi("2147483648"))

s =Solution()
print(s.myAtoi("-0012a42"))

s =Solution()
print(s.myAtoi("+0018"))

