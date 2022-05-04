import heapq
import bisect

class Solution:
    def findKthLargest(self, nums: 'list[int]', k: int) -> int:
        '''
        Given an integer array nums and an integer k, 
        return the kth largest element in the array.

        Note that it is the kth largest element in the sorted order, 
        not the kth distinct element.
        
        '''
        cnt, p = 0, None
        for i in sorted(nums)[::-1]:
            if i != p:
                cnt += 1
                p = i
            else:
                continue
            if cnt == k:
                return i
        return i

       
            

obj = Solution()
nums = [3,2,1,5,6,4]
k = 2
ans = obj.findKthLargest(nums, k)
print(ans)

