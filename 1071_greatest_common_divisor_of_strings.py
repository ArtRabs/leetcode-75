# LeetCode 1071 Greatest Common Divisor of Strings
# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(len(str1), len(str2))
        return str1[:g]

if __name__ == "__main__":

    print(Solution().gcdOfStrings("ABCABC", "ABC"))
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))
    print(Solution().gcdOfStrings("LEET", "CODE")) 
    print(Solution().gcdOfStrings("AAAAAB", "AAA"))
    print(Solution().gcdOfStrings("ABABABAB", "ABAB"))
    print(Solution().gcdOfStrings("AAAAAAAAA", "AAACCC"))
    print(Solution().gcdOfStrings("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))





# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """

#         i = 1

#         gcd_str2 = False

#         gcd_str = ""

#         if str1 + str2 != str2 + str1:

#             return ""

#         while len(str1) > len(gcd_str):

#             gcd_str += str2[:i]

#             if gcd_str == str2:
                
#                 gcd_str2 = True

#             if gcd_str == str1:

#                 if gcd_str2 and len(str1) % len(str2) == 0:

#                     gcd_str = str2

#                     return str2

#                 return str2[:i]

#             if str2[:i] == str1:

#                 str = 2

#                 return str2[:i]

#             if i > len(str1):

#                 if str1 + str2 != str2 + str1:

#                     return ""

#                 return ""
            
#             if len(gcd_str) >= len(str1):

#                 i += 1
#                 gcd_str = ""
    
