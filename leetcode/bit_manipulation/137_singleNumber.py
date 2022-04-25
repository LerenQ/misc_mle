from functools import reduce

class Solution:
    def singleNumber(self, nums: 'list[int]') -> int:
        '''
        Given a non-empty array of integers nums, 
        every element appears three times except for one. Find that single one.

        You must implement a solution with a linear runtime complexity 
        and use only constant extra space.
        
        '''
        return reduce(lambda x, y: x ^ y, nums)


test = Solution()
nums = [0,1,0,1,0,1,99]
ans = test.singleNumber(nums)
print(ans)