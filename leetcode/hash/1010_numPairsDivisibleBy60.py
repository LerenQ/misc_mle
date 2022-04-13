import collections
class Solution:
    def numPairsDivisibleBy60(self, time: 'list[int]') -> int:
        '''
        You are given a list of songs where the ith song has a duration of time[i] seconds.
        Return the number of pairs of songs for 
        which their total duration in seconds is divisible by 60. 
        Formally, we want the number of indices i, j 
        such that i < j with (time[i] + time[j]) % 60 == 0.
        
        '''
        c = collections.defaultdict(int)
        ans = 0
        for t in time:
            ans += c[-t % 60]
            c[t%60] += 1
        return ans
        

test = Solution()
time = [30,20,150,100,40]
ans = test.numPairsDivisibleBy60(time)
print(ans)