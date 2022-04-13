from bisect import bisect_left 


class Solution:
    def searchInsert(self, nums: 'list[int]', target: int) -> int:
        '''
        Given a sorted array of distinct integers and a target value, 
        return the index if the target is found. If not, 
        return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        '''
        idx = bisect_left(nums, target)

        return idx
        

test = Solution()
nums = [1,3,5,6]
target = 2
ans = test.searchInsert(nums, target)
print(ans)