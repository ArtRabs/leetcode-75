# LeetCode 1372 Longest ZigZag Path in a Binary Tree
# URL: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Difficulty: Medium 
# Language: Python 3.10+ 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.zigzag = 0

        def dfs(node, lefting, length):

            if not node:

                return
            
            self.zigzag = max(self.zigzag, length)
            
            if lefting:

                dfs(node.left, False, length + 1)            
                dfs(node.right, True, 1)

            else:

                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.zigzag
        