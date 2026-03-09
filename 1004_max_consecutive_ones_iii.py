# LeetCode 1004 Max Consecutive Ones III
# URL: https://leetcode.com/problems/max-consecutive-ones-iii/
# Difficulty: Medium
# Language: Python 3.10+

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):

            if nums[right] == 0:

                zero_count += 1

            while zero_count > k:

                if nums[left] == 0:

                    zero_count -= 1

                left += 1

            if max_length < right - left + 1:

                max_length = right - left + 1

        return max_length
    

if __name__ == "__main__":

    # print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
    print(Solution().longestOnes([0,0,1,1,1,0,0], 0)) # 3
    print(Solution().longestOnes([1,1,1], 0)) # 3
    print(Solution().longestOnes([1,0,1,1,0,1], 2)) # 6
    print(Solution().longestOnes([0,0,0,1], 4)) # 4