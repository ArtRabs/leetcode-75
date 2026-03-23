# LeetCode 872 Leaf-Similar Trees
# URL: https://leetcode.com/problems/leaf-similar-trees/
# Difficulty: Easy 
# Language: Python 3.10+ 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(node, leaves):

            if not node:

                return
            
            if not node.left and not node.right:

                leaves.append(node.val)

            dfs(node.left, leaves)

            dfs(node.right, leaves)

        leaves1, leaves2 = [], []

        dfs(root1, leaves1)

        dfs(root2, leaves2)
        
        return leaves1 == leaves2

    


# class Solution(object):
#     def leafSimilar(self, root1, root2):
#         """
#         :type root1: Optional[TreeNode]
#         :type root2: Optional[TreeNode]
#         :rtype: bool
#         """
        
#     def leafSimilar(self, root1, root2):

#         def dfs(node):

#             if not node: 
                
#                 return

#             if not node.left and not node.right: 

#                 yield node.val

#             for i in dfs(node.left): 

#                 yield i

#             for i in dfs(node.right): 

#                 yield i
                
#         return all(a == b for a, b in itertools.izip_longest(dfs(root1), dfs(root2)))