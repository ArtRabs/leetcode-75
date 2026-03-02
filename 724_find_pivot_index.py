# LeetCode 724 Find Pivot Index
# URL: https://leetcode.com/problems/find-pivot-index/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sumAll = sum(nums)
        sumLeft = 0

        for i, num in enumerate(nums):

            sumRight = sumAll - sumLeft - num

            if sumLeft == sumRight:

                return i

            sumLeft += num

        return -1


if __name__ == "__main__":

    print(Solution().pivotIndex([1,7,3,6,5,6]))
    print(Solution().pivotIndex([1,2,3]))
    print(Solution().pivotIndex([2,1,-1]))
    print(Solution().pivotIndex([5,7,7,8,8,10]))
    print(Solution().pivotIndex([1,2,3,4,5,6]))


# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         len_nums = len(nums)

#         i = 0

#         while i < len_nums:

#             sumLeft = sum(nums[i : i + 1])
#             sumRight = sum(nums[i + 1 : len_nums - 1])

#             if  sumLeft == sumRight:

#                 return i

#             i += 1

#         return -1   