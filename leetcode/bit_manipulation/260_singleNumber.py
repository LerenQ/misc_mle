from functools import reduce

class Solution:
    def singleNumber(self, nums: 'list[int]') -> int:
        '''
        Given an integer array nums, 
        in which exactly two elements appear only once 
        and all the other elements appear exactly twice. 
        
        Find the two elements that appear only once. 
        You can return the answer in any order.
        You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

        
        '''       
        mask = 1
        sumtwo = self.xor(nums)
        while sumtwo&mask == 0:
            mask <<= 1
        n1 = [num for num in nums if mask&num != 0]
        n2 = [num for num in nums if mask&num == 0]
        return [self.xor(n1), self.xor(n2)]


    def xor(self,n):
        from functools import reduce
        return reduce(lambda x, y: x ^ y, n)

        


test = Solution()
nums = [0,1,0,1,99,98]
ans = test.singleNumber(nums)
print(ans)