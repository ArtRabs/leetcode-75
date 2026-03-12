# LeetCode 2352 Equal Row and Column Pairs
# URL: https://leetcode.com/problems/equal-row-and-column-pairs/
# Difficulty: Medium 
# Language: Python 3.10+

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        from collections import Counter

        row_counts = Counter(tuple(row) for row in grid)
        col_counts = Counter(tuple(col) for col in zip(*grid))

        count = 0

        for row_tuple, row_freq in row_counts.items():

            count += row_freq * col_counts.get(row_tuple, 0)

        return count

if __name__ == "__main__":

    print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
    print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
            
    




# class Solution(object):
#     def equalPairs(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
        
#         count = 0

#         for i in range(len(grid)):

#             for j in range(len(grid[0])):

#                 if grid[i] == [grid[k][j] for k in range(len(grid))]:

#                     count += 1
                    
#         return count






# class Solution(object):
#     def equalPairs(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
        
#         count = 0

#         columns = [list(c) for c in zip(*grid)]

#         i = 0

#         while i < len(grid):

#             if columns[i] in grid:

#                 count += 1

#             i += 1
        
#         return count