# LeetCode 933 Number of Recent Calls
# URL: https://leetcode.com/problems/number-of-recent-calls/
# Difficulty: Easy 
# Language: Python 3.10+ 

class RecentCounter(object):

    def __init__(self):
        
        self.records = []
        self.start_time = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.records.append(t)

        while self.records[self.start_time] < t - 3000:

            self.start_time += 1

        return len(self.records) - self.start_time
    
if __name__ == "__main__":

    recent_counter = RecentCounter()
    print(recent_counter.ping(1))
    print(recent_counter.ping(100))
    print(recent_counter.ping(3001))
    print(recent_counter.ping(3002))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)