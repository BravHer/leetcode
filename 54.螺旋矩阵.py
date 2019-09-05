'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]


'''


# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         res = []
#         if not matrix or len(matrix) == 0:
#             return res
#         left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
#         while True:
#             for i in range(left, right + 1):
#                 res.append(matrix[top][i])
#             top += 1
#             if top > bottom:
#                 break
#
#             for i in range(top, bottom + 1):
#                 res.append(matrix[i][right])
#             right -= 1
#             if left > right:
#                 break
#
#             for i in range(right, left - 1, -1):
#                 res.append(matrix[bottom][i])
#             bottom -= 1
#             if top > bottom:
#                 break
#
#             for i in range(bottom, top - 1, -1):
#                 res.append(matrix[i][left])
#             left += 1
#             if left > right:
#                 break
#         return res

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return None
        x0 = y0 = 0
        xn = len(matrix)
        yn = len(matrix[0])
        res = []

        while x0 < xn and y0 < yn:
            for y in range(y0, yn):
                res.append(matrix[x0][y])

            for x in range(x0 + 1, xn):
                res.append(matrix[x][yn - 1])

            if x0 < xn - 1:
                for y in range(yn - 2, y0 - 1  , -1):
                    res.append(matrix[xn - 1][y])

            if y0 < yn - 1:
                for x in range(xn - 2, x0, -1 ):
                    res.append((matrix[x][y0]))

            y0 = y0 + 1
            yn = yn - 1
            x0 = x0 + 1
            xn = xn - 1

        return res