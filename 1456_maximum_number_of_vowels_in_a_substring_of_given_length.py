# LeetCode 1456 Maximum Number of Vowels in a Substring of Given Length
# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Difficulty: Medium
# Language: Python 3.10+

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_vowels = 0
        current_vowels = 0

        vowel = "aeiou" + "AEIOU"

        for i in range(k):

            if s[i] in vowel:

                current_vowels += 1

        max_vowels = current_vowels

        for i in range(k, len(s)):

            if s[i] in vowel:

                current_vowels += 1

            if s[i - k] in vowel:

                current_vowels -= 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
    
if __name__ == "__main__":

    print(Solution().maxVowels("abciiidef", 3))
    print(Solution().maxVowels("aeiou", 2))
    print(Solution().maxVowels("leetcode", 3))