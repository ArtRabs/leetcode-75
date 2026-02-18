# LeetCode 1768 Merge Strings Alternately
# URL: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Language: Python 3


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        len_word1 = len(word1)
        len_word2 = len(word2)

        merged_word = ""

        i = 0

        while len_word1 != 0 or len_word2 != 0:

            if len_word1 > 0:
                merged_word += word1[i]
                len_word1 -= 1

            if len_word2 > 0:
                merged_word += word2[i]
                len_word2 -= 1

            i += 1

        return merged_word

        
if __name__ == "__main__":

    print(Solution().mergeAlternately("abc", "xyz"))
    print(Solution().mergeAlternately("abcdefg", "xyz"))
    print(Solution().mergeAlternately("abc", "tuvwxyz"))