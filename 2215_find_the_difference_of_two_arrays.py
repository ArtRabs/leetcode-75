# LeetCode 2215 Find the Difference of Two Arrays
# URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Difficulty: Easy
# Language: Python 3.10+ 

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        difference_nums = []

        current_nums = []

        for num in set(nums1):

            if num not in nums2:

                current_nums.append(num)

        difference_nums.append(current_nums)

        current_nums = []

        for num in set(nums2):

            if num not in nums1:

                current_nums.append(num)

        difference_nums.append(current_nums)

        return difference_nums
    
if __name__ == "__main__":

    print(Solution().findDifference([1,2,3], [2,4,6]))
    print(Solution().findDifference([1,2,3,3], [1,1,2,2]))