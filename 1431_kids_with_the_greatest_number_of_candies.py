# LeetCode 1431 Kids With the Greatest Number of Candies
# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest_kids = []
        max_candy = max(candies)

        for candy in candies:

            greatest_kid = candy + extraCandies >= max_candy
            greatest_kids.append(greatest_kid)
        
        return greatest_kids