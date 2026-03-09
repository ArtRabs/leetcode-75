# LeetCode 1679 Max Number of K-Sum Pairs
# URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Difficulty: Medium
# Language: Python 3.10+ 

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = {}      
        ops = 0
        for x in nums:
            need = k - x
            if freq.get(need, 0) > 0:

                ops += 1
                freq[need] -= 1
                if freq[need] == 0:
                    del freq[need]
            else:

                freq[x] = freq.get(x, 0) + 1

        return ops
    
    
if __name__ == "__main__":

    print(Solution().maxOperations([1,2,3,4], 5)) # 2
    print(Solution().maxOperations([3,1,3,4,3], 6)) # 1


# class Solution(object):
#     def maxOperations(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """

#         pairs = 0
#         seen_pair_index = set()

#         left = 0
#         right = 0

#         while left < len(nums) - 1:

#             right = left + 1

#             while right < len(nums):

#                 while right in seen_pair_index:

#                     right += 1

#                 if right == len(nums):

#                     break

#                 if (nums[left] + nums[right]) == k:

#                     pairs += 1
#                     seen_pair_index.add(right)
#                     seen_pair_index.add(left)

#                     right += 1

#                     break

#                 else:

#                     right += 1

#             left += 1

#             while left in seen_pair_index:

#                 left += 1

#         return pairs
    



