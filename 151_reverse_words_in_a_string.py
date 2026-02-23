# LeetCode 151 Reverse Words in a String
# URL: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        split_words = s.split()

        reverse_words = ""

        for word in split_words:

            if reverse_words:

                reverse_words = word + " " + reverse_words

            else:

                reverse_words = word  
        
        return reverse_words
    
if __name__ == "__main__":

    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world!  "))
    print(Solution().reverseWords("a good   example"))