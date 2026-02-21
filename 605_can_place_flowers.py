# LeetCode 605 Can Place Flowers
# URL: https://leetcode.com/problems/can-place-flowers/
# Difficulty: Easy
# Language: Python 3.10+

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0

        if len(flowerbed) == 1:

            if flowerbed[i] == 0 and n == 1:

                n -= 1

                if n == 0:

                    return True
            
            elif flowerbed[i] == 1 and n == 0:

                return True
            
            elif flowerbed[i] == 0 and n == 0:

                return True

            else:

                return False

        while i < len(flowerbed) and n != 0:

            if i != 0:

                # Checks the last part of list
                if i == len(flowerbed) - 1:

                    if flowerbed[i - 1] == 0 and flowerbed[i] == 0:

                        n -= 1

                        flowerbed[i] = 1

                # Checks everything except first and last part of string
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:

                    n -= 1

                    flowerbed[i] = 1

            if i == 0:

                # Checks first part of the string
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:

                    n -= 1

                    flowerbed[i] = 1

            i += 1

        if n == 0:

            return True

        else:

            return False
        
        

if __name__ == "__main__":

    print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
    print(Solution().canPlaceFlowers([0,0,1,0,1], 1))
    print(Solution().canPlaceFlowers([1,0,1,0,0], 1))
    print(Solution().canPlaceFlowers([1], 1))


        # for flower in flowerbed:

        #     if flower == 1:

        #         is_flower = True
        #         flower_duration = 2

        #     if flower == 0:

        #         is_empty_flower = True
        #         empty_flower_duration = 2

        #     if flower_duration == 0:
                
        #         is_flower = False

        #     if empty_flower_duration == 0:

        #         is_empty_flower = False

        #     flower_duration -= 1
        #     empty_flower_duration -= 1