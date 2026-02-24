# LeetCode 283 Move Zeroes
# URL: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)

        i = 0
        
        for num in nums:

            if num != 0:

                nums[i] = num
                
                i += 1
            
        zero = -1 * (len_nums - i)

        while zero < 0:

            nums[zero] = 0

            zero += 1


if __name__ == "__main__":

    Solution().moveZeroes([0,1,0,3,12])
    Solution().moveZeroes([0])
