# LeetCode 2130 Maximum Twin Sum of a Linked List
# URL: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Difficulty: Medium 
# Language: Python 3.10+

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None

        previous = None

        while fast is not None:

            next_node = fast.next

            fast.next = previous

            previous = fast

            fast = next_node

        max_twin_sum = 0

        while previous is not None:

            node1 = previous.val
            node2 = head.val

            twin_sum = node1 + node2

            max_twin_sum = max(twin_sum, max_twin_sum)

            previous = previous.next
            head = head.next

        return max_twin_sum
    