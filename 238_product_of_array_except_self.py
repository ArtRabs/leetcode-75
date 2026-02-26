# LeetCode 238 Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Language: Python 3.10+

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)                # how many numbers are in the list
        result = [1] * n             # start with a list of 1s

        # Step 1: build products of everything to the LEFT of each index
        left_product = 1
        for i in range(n):
            result[i] = left_product   # store product so far
            left_product *= nums[i]    # update product by multiplying current number

        # Step 2: build products of everything to the RIGHT of each index
        right_product = 1
        for i in range(n - 1, -1, -1):   # loop backwards from last index to 0
            result[i] *= right_product   # multiply left product by right product
            right_product *= nums[i]     # update right product

        return result 


if __name__ == "__main__":

    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([-1,1,0,-3,3]))
    print(Solution().productExceptSelf([4,5,6,7]))
    print(Solution().productExceptSelf([-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,1,1]))


# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
#         product_except_self = [1] * len(nums)

#         i = 0
#         j = 0

#         for num in nums:

#             while len(nums) > j:
                
#                 if i != j:

#                     product_except_self[j] *= num

#                 j += 1

#             i += 1
#             j = 0

#         i = 0

#         return product_except_self


# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         result = [1] * n
        
#         # Compute prefix products
#         prefix = 1
#         for i in range(n):
#             result[i] = prefix
#             prefix *= nums[i]
        
#         # Compute suffix products and multiply with prefix
#         suffix = 1
#         for i in range(n - 1, -1, -1):
#             result[i] *= suffix
#             suffix *= nums[i]
        
#         return result