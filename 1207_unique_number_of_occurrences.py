# LeetCode 1207 Unique Number of Occurrences
# URL: https://leetcode.com/problems/unique-number-of-occurrences/
# Difficulty: Easy
# Language: Python 3.10+ 

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        current_arr = []
        index_arr = []
        
        for num in arr:

            # Checks if the number is already seen
            if num not in current_arr:

                current_arr.append(num)
                index_arr.append(0)

            # If the number is seen before, add a counter of occurence
            elif num in current_arr:
                
                index = current_arr.index(num)
                index_arr[index] += 1

        # Checks if there are duplicates, if none are duplicates then both len are the same
        if len(current_arr) == len(set(index_arr)):

            return True

        else:

            return False
        
if __name__ == "__main__":

    print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
    print(Solution().uniqueOccurrences([1,2]))
    print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))