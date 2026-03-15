# LeetCode 394 Decode String
# URL: https://leetcode.com/problems/decode-string/
# Difficulty: Medium 
# Language: Python 3.10+ 

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        current_string = ""
        current_num = 0

        for char in s:

            if char.isdigit():

                current_num = current_num * 10 + int(char)

            elif char == "[":
                
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0

            elif char == "]":

                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string

            else:

                current_string += char

        return current_string
    
if __name__ == "__main__":

    print(Solution().decodeString("3[a]2[bc]"))
    print(Solution().decodeString("3[a2[c]]"))
    print(Solution().decodeString("2[abc]3[cd]ef"))