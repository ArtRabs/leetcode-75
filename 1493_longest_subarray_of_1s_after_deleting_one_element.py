# LeetCode 1493 Longest Subarray of 1's After Deleting One Element
# URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Difficulty: Medium
# Language: Python 3.10+ 

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        len_nums = len(nums)

        max_length = 0
        left = 0
        zero_count = 0

        for right in range(len_nums):

            if nums[right] == 0:

                zero_count += 1

            while zero_count > 1:

                if nums[left] == 0:

                    zero_count -= 1

                left += 1
        
            max_length = max(max_length, right - left)

        return max_length
    
if __name__ == "__main__":

    # print(Solution().longestSubarray([1,1,0,1]))
    # print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
    print(Solution().longestSubarray([1,1,1]))
    print(Solution().longestSubarray([1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1]))