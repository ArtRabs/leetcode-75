# LeetCode 1448 Count Good Nodes in Binary Tree
# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium 
# Language: Python 3.10+ 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, max_node):

            if node is None:

                return 0

            # checks if node is good
            # good is >= root
            if node.val >= max_node:

                count = 1

            else:

                count = 0

            # update max
            new_max = max(max_node, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)