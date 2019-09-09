'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        A = [[0]*n for _ in range(n)]

        i = j = 0
        k=1
        while not A[i][j]:
            while j<=n-1 and A[i][j]==0:
                A[i][j]=k
                k+=1
                j+=1

            j-=1
            i+=1
            while i<=n-1 and A[i][j]==0:
                A[i][j]=k
                k+=1
                i+=1

            i-=1
            j-=1
            while j>=0 and A[i][j]==0:
                A[i][j]=k
                k+=1
                j-=1

            i-=1
            j+=1
            while i>=0 and A[i][j]==0:
                A[i][j]=k
                k+=1
                i-=1
            i+=1
            j+=1
        return A




dp = [[1,2,3],[5,6,7]]
print(dp[0][2])
print(dp[1])
dp.append(6)
print(dp)
dp.append([7,8])
print(dp)
