from functools import reduce

class Solution:
    def singleNumber(self, nums: 'list[int]') -> int:
        '''
        Given a non-empty array of integers nums, 
        every element appears three times except for one. Find that single one.

        You must implement a solution with a linear runtime complexity 
        and use only constant extra space.
        
        '''       
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                if ((num >> i) & 1):
                    count += 1
            ans |= ((count%3!=0) << i)
        return self.convert(ans)
    
    def convert(self, x):
            if x >= 2**31:
                x -= 2**32
            return x

        


test = Solution()
nums = [0,1,0,1,0,1,99]
ans = test.singleNumber(nums)
print(ans)