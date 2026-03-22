# LeetCode 104 Maximum Depth of Binary Tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy 
# Language: Python 3.10+ 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if root is None:

            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))