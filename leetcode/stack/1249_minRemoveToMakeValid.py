from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Given a string s of '(' , ')' and lowercase English characters.
        Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
        so that the resulting parentheses string is valid and return any valid string.

        Formally, a parentheses string is valid if and only if:
            It is the empty string, contains only lowercase characters, or
            It can be written as AB (A concatenated with B), where A and B are valid strings, or
            It can be written as (A), where A is a valid string.
        
        '''

        q = deque()
        for k, val in enumerate(s):
            if val == '(':
                q.append((k, val))
            elif val == ')' and ((len(q) == 0) or (q[-1][1] != '(')):
                q.append((k, val))
            elif val == ')' and q[-1][1] == '(':
                q.pop()
            else:
                pass
        
        if len(q) != 0:
            ans = s[0:q[0][0]]
            for i in range(len(q)-1):
                ans += s[q[i][0]+1:q[i+1][0]]
            ans += s[q[-1][0]+1:]
            return ans
        else:
            return s
                
        
        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
s = "lee(t(c)o)de)"
s = 'abc'
ans = obj.minRemoveToMakeValid(s)
print(ans)

