class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Write a function that takes an unsigned integer and 
        returns the number of '1' bits it has (also known as the Hamming weight).
        
        '''
        ans, mask = 0, 1
        for _ in range(32):
            if n & mask != 0:
                ans += 1
            mask <<= 1        
        return ans


test = Solution()
n = 11
ans = test.hammingWeight(n)
print(ans)