# LeetCode 450 Delete Node in a BST
# URL: https://leetcode.com/problems/delete-node-in-a-bst/
# Difficulty: Medium 
# Language: Python 3.10+ 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        if not root:

            return None

        if root.val > key:

            root.left = self.deleteNode(root.left, key)

        elif root.val < key:

            root.right = self.deleteNode(root.right, key)

        else:

            if not root.left:

                return root.right

            elif not root.right:

                return root.left

            else:

                min_node = root.right

                while min_node.left:

                    min_node = min_node.left

                root.val = min_node.val

                root.right = self.deleteNode(root.right, min_node.val)

        return root