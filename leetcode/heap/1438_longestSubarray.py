import bisect

import heapq

class Solution:
    def longestSubarray(self, nums: 'list[int]', limit: int) -> int:
        '''
        Given an array of integers nums and an integer limit, 
        return the size of the longest non-empty subarray 
        such that the absolute difference between any two elements of this subarray is less than or equal to limit.
        
        '''
        maxd, mind = [], []
        res = i = 0
        for j, a in enumerate(nums):
            heapq.heappush(maxd, (-a, j))
            heapq.heappush(mind, (a, j))
            # print(maxd, '--', mind)
            while -maxd[0][0] - mind[0][0] > limit:
                # print(maxd, '--', mind)
                i = min(maxd[0][1], mind[0][1]) + 1
                while maxd[0][1] < i: heapq.heappop(maxd)
                while mind[0][1] < i: heapq.heappop(mind)
            # print(maxd, '--', mind)
            res = max(res, j - i + 1)
        return res




obj = Solution()
nums = [4,2,2,2,4,4,2,2]
nums = [10,1,2,4,7,2]
limit = 0
limit = 5
ans = obj.longestSubarray(nums, limit)
print(ans)