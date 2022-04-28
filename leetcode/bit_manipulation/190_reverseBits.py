from typing import AnyStr


class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Reverse bits of a given 32 bits unsigned integer.
        
        '''

        l = [i for i in bin(n)]
        ans = []
        for i in reversed(l):
            ans.append(i)
        ans.pop(-1)
        ans.pop(-1)
        while len(ans) < 32:
            ans.append('0')
        rslt = ''.join(ans)
        return int(rslt,2)


test = Solution()
n = 43
ans = test.reverseBits(n)
print(ans)