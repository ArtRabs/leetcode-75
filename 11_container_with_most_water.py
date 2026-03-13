# LeetCode 11 Container With Most Water
# URL: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium 
# Language: Python 3.10+ 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height [left] < height[right]:

                left += 1

            else:

                right -= 1

        return max_area
    

if __name__ == "__main__":

    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
    print(Solution().maxArea([1,1]))





# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
        
#         left, right = 0, len(height) - 1
#         max_area = 0

#         while left < right:

#             width = right - left
#             current_height = min(height[left], height[right])
#             current_area = width * current_height

#             max_area = max(max_area, current_area)

#             if height[left] < height[right]:

#                 left += 1

#             else:

#                 right -= 1

#         return max_area




# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """

#         max_area = 0

#         for left in range(len(height)):

#             for right in range(left + 1, len(height)):

#                 current_area = (right - left) * min(height[left], height[right])
#                 max_area = max(max_area, current_area)

#         return max_area