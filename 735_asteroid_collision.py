# LeetCode 735 Asteroid Collision
# URL: https://leetcode.com/problems/asteroid-collision/
# Difficulty: Medium 
# Language: Python 3.10+ 

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:

            while stack and asteroid < 0 < stack[-1]:

                if stack[-1] < -asteroid:

                    stack.pop()

                    continue

                elif stack[-1] == -asteroid:

                    stack.pop()

                break

            else:

                stack.append(asteroid)

        return stack
    

if __name__ == "__main__":

    print(Solution().asteroidCollision([5, 10, -5]))
    print(Solution().asteroidCollision([8, -8]))
    print(Solution().asteroidCollision([10, 2, -5]))