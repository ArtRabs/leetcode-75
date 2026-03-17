# LeetCode 649 Dota2 Senate
# URL: https://leetcode.com/problems/dota2-senate/
# Difficulty: Medium 
# Language: Python 3.10+

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        from collections import deque

        radiant = deque()
        dire = deque()
        n = len(senate)

        for i in range(n):

            if senate[i] == "R":

                radiant.append(i)

            elif senate[i] == "D":

                dire.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:

                radiant.append(r + n)

            if r > d:

                dire.append(d + n)

        if radiant:

            return "Radiant"

        elif dire:

            return "Dire"


if __name__ == "__main__":

    print(Solution().predictPartyVictory("RD"))
    print(Solution().predictPartyVictory("RDD"))
    print(Solution().predictPartyVictory("DDRRR"))