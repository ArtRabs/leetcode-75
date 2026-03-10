# LeetCode 2390 Removing Stars From a String
# URL: https://leetcode.com/problems/removing-stars-from-a-string/
# Difficulty: Medium
# Language: Python 3.10+ 

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for char in s:

            if char != "*":

                stack.append(char)

            else:

                stack.pop()

        return "".join(stack)
        
if __name__ == "__main__":

    print(Solution().removeStars("leet**cod*e"))