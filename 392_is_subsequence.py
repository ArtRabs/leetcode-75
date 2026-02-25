# LeetCode 392 Is Subsequence
# URL: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        len_s = len(s)
        
        i = 0

        if s == "":

            return True

        for letter in t:

            if letter == s[i]:

                i += 1 

            if len_s == i:

                return True    

        return False
        

if __name__ == "__main__":

    print(Solution().isSubsequence("abc", "ahbgdc"))    
    print(Solution().isSubsequence("axc", "ahbgdc"))
    print(Solution().isSubsequence("", "ahbgdc"))
    print(Solution().isSubsequence("b","abc"))