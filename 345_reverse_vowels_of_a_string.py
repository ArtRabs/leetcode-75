# LeetCode 345 Reverse Vowels of a String
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Getting vowels

        vowels = []
        vowel = "aeiou" + "AEIOU"

        for letter in s:

            if letter in vowel:

                vowels.append(letter)

        # Sorting vowels

        i = 0
        j = len(vowels) - 1

        reversed_vowels = [None] * len(vowels)
        len_vowels = len(vowels)

        while i < len_vowels:

            reversed_vowels[i] = vowels[j]

            i += 1
            j += -1

        # Putting the sorted vowels

        k = 0

        new_s = ""

        for letter in s:

            if letter in vowel:

                new_s += reversed_vowels[k]
                k += 1

            else:

                new_s += letter

        return new_s
        

if __name__ == "__main__":

    print(Solution().reverseVowels("Icecream"))
    print(Solution().reverseVowels("ocACreemI"))