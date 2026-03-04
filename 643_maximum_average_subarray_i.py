# LeetCode 643 Maximum Average Subarray I
# URL: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy
# Language: Python 3.10+ 

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        len_nums = len(nums)

        if len_nums == 0 or k == 0:

            return 0.0

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len_nums):

            window_sum += nums[i] - nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / float(k)
    
    
if __name__ == "__main__":

    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
    print(Solution().findMaxAverage([5], 1))



# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
        
#         len_nums = len(nums)

#         highest_average = 0
        
#         i = 0
#         k_index = k

#         while len_nums > k - 1:

#             sum_nums = sum(nums[i:k])

#             average_nums = sum_nums / k_index

#             if average_nums > highest_average:

#                 highest_average = average_nums

#             i += 1
#             k += 1

#         return highest_average


# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
        
#         len_nums = len(nums)

#         highest_average = float('-inf')
        
#         i = 0
#         k_index = k

#         while len_nums > k - 1:

#             sum_nums = sum(nums[i:k])

#             average_nums = sum_nums / float(k_index)

#             if average_nums > highest_average:

#                 highest_average = average_nums

#             i += 1
#             k += 1

#         return highest_average
    