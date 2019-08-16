'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 组合排列
'''class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n -2
        xroad = m - 1
        return self.arrangement(total, min(xroad, total - xroad))

    def arrangement(self, n, m):
        o = 1
        p = 1
        q = 1
        for i in range(1, n + 1):
            o = o * i
            if i <= m:
                p = p * i
            if i <= n - m:
                q = q * i
        return int(o / (p * q))
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * n for _ in range(m)]
        # print(memo)
        return self.dfs(m - 1, n - 1, memo)

    def dfs(self, m, n, memo):
        if m == 0 or n == 0:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, memo)
        left = self.dfs(m, n - 1, memo)
        memo[m][n] = up + left
        return memo[m][n]




s = Solution()
print(s.uniquePaths(3,2))

s = Solution()
print(s.uniquePaths(7,3))