# LeetCode 443 String Compression
# URL: https://leetcode.com/problems/string-compression/
# Difficulty: Medium
# Language: Python 3.10+

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n == 0:
            return 0

        write = 0   # position to write the next compressed character/digit
        read = 0    # position to read the input

        while read < n:
            current_char = chars[read]
            count = 0

            # Count how many times current_char repeats starting at read
            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # If count > 1, write each digit of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # write is the new length
        return write

        
if __name__ == "__main__":

    print(Solution().compress(["a","a","b","b","c","c","c"]))
    print(Solution().compress(["a"]))
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """

#         extended_chars = chars + [""]

#         list_char = []

#         current_char = ""
#         count = 0
#         new_char = False

#         for char in extended_chars:

#             if list_char == [""]:

#                 list_char.pop()
                           
#             if char != current_char:

#                 new_char = True

#             if new_char:

#                 list_char.append(current_char)

#                 current_char = char 

#                 if count > 1:

#                     str_count = str(count)

#                     list_count = list(str_count)

#                     for num in list_count:

#                         list_char.append(num)

#                 count = 0
#                 new_char = False               

#             if char == current_char:

#                 count += 1

#         return len(list_char), list_char


# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """
#         if not chars:
#             return []

#         list_char = []
#         current_char = chars[0]
#         count = 1

#         for char in chars[1:]:
#             if char == current_char:
#                 count += 1
#             else:
#                 list_char.append(current_char)
#                 if count > 1:
#                     list_char.extend(list(str(count)))
#                 current_char = char
#                 count = 1

#         # append the final group
#         list_char.append(current_char)
#         if count > 1:
#             list_char.extend(list(str(count)))

#         return list_char

