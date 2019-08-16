'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.re = -2 ** 31

        self.robot(root)
        return self.re

    def robot(self, root):
        if root == None:
            return 0
        left = max(0, self.robot(root.left))
        right = max(0, self.robot(root.right))
        self.re = max(self.re, root.val + left + right)
        return max(root.val, root.val + max(left, right))


