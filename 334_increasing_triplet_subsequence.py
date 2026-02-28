# LeetCode 334 Increasing Triplet Subsequence
# URL: https://leetcode.com/problems/increasing-triplet-subsequence/
# Difficulty: Medium
# Language: Python 3.10+

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        i = 10**18
        j = 10**18
        k = 0

        for num in nums:

            if num <= i:

                i = num
            
            elif num <= j:

                j = num

            elif j <= num:

                k = num
                
                print(i, j, k)

                break

        if i < j and j < k:

            return True
        
        else:

            return False


if __name__ == "__main__":

    print(Solution().increasingTriplet([1,2,3,4,5]))
    print(Solution().increasingTriplet([20,100,10,12,5,13]))
    print(Solution().increasingTriplet([5,4,3,2,1]))
    print(Solution().increasingTriplet([2,1,5,0,4,6]))


# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         i = nums[0]
#         j = 0
#         j_first = True
#         k = 0
#         k_first = True

#         for num in nums:

#             if i < num:

#                 if j_first and i < num:

#                     j = num

#                     j_first = False

#                 elif k_first and i < j and j < num:

#                     k = num

#                     k_first = False

#         if i < j and j < k:

#             return True
        
#         else:

#             return False