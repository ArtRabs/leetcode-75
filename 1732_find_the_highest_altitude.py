# LeetCode 1732 Find the Highest Altitude
# URL: https://leetcode.com/problems/find-the-highest-altitude/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        total_altitude = 0
        highest_altitude = 0

        for altitude in gain:

            total_altitude += altitude

            if highest_altitude < total_altitude:

                highest_altitude = total_altitude

        return highest_altitude
    
if __name__ == "__main__":

    print(Solution().largestAltitude([-5,1,5,0,-7]))