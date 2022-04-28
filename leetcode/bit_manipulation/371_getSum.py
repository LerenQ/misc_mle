import numpy as np

class Solution:
    def getSum(self, a, b) -> int:
        '''
        Given two integers a and b, 
        return the sum of the two integers without using the operators + and -.

        
        '''       
        

        while b != 0:
            a, b = np.int32(a ^ b), np.int32((a & b) << 1)
        return int(a)


test = Solution()
a = 2
b = 3
ans = test.getSum(a, b)
print(ans)