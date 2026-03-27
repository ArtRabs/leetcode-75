# LeetCode 437 Path Sum III
# URL: https://leetcode.com/problems/path-sum-iii/
# Difficulty: Medium 
# Language: Python 3.10+

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        def paths_from(node, remaining):

            if not node:

                return 0
            
            cnt = 0

            if node.val == remaining:

                cnt += 1

            cnt += paths_from(node.left, remaining - node.val)
            cnt += paths_from(node.right, remaining - node.val)

            return cnt

        if not root:

            return 0
        
        # count paths starting at root plus paths in left and right subtrees
        return paths_from(root, targetSum) + \
               self.pathSum(root.left, targetSum) + \
               self.pathSum(root.right, targetSum)
    

# class Solution(object):
#     def pathSum(self, root, targetSum):
#         """
#         :type root: Optional[TreeNode]
#         :type targetSum: int
#         :rtype: int
#         """
        
#         # total paths that have the target sum
#         self.sum_paths = 0

#         # 1st layer DFS
#         self.dfs(root, targetSum)

#         return self.sum_paths

#     # traverse the tree, for each treecode call another DFS to check the target sum
#     def dfs(self, node, targetSum):

#         if node is None:

#             return
        
#         self.test(node, targetSum)
#         self.dfs(node.left, targetSum)
#         self.dfs(node.right, targetSum)

#     # checks the target sum, add 1 to the sum_paths if it is
#     def test(self, node, targetSum):

#         if node is None:

#             return

#         if node.val == targetSum:

#             self.sum_paths += 1

#         self.test(node.left, targetSum - node.val)
#         self.test(node.right, targetSum - node.val)
