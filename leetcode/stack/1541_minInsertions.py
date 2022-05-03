class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Given a parentheses string s containing only the characters '(' and ')'. 
        A parentheses string is balanced if:

        Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
        Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
        
        '''
        
        cnt, rp = 0, 0

        for i in s:
            if i == '(':
                if rp&1 == 1:
                    cnt += 1
                    rp -= 1
            
                rp += 2

            else:
                rp -= 1
                if rp < 0:
                    cnt += 1
                    rp += 2

        return cnt + rp        
    

obj = Solution()
s = "))(()()))("
ans = obj.minInsertions(s)
print(ans)

