# LeetCode 1657 Determine if Two Strings Are Close
# URL: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium
# Language: Python 3.10+ 

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        if len(word1) != len(word2):

            return False

        if set(word1) != set(word2):

            return False

        from collections import Counter

        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())
        
        return freq1 == freq2
    
if __name__ == "__main__":

    print(Solution().closeStrings("abc", "bca"))
    print(Solution().closeStrings("a", "aa"))
    print(Solution().closeStrings("cabbba", "abbccc"))
    print(Solution().closeStrings("abbzzca", "babzzcz"))




# class Solution(object):
#     def closeStrings(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: bool
#         """
        
#         if len(word1) != len(word2):

#             return False
    
#         for char in set(word1):

#             if char not in word2:

#                 return False

#         return True