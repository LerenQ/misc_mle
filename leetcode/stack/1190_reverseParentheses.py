from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        You are given a string s that consists of lower case English letters and brackets.
        Reverse the strings in each pair of matching parentheses, starting from the innermost one.
        Your result should not contain any brackets.
        
        '''

        ans = deque([''])
        for i in s:
            if i == '(':
                ans.append('')
            elif i == ')':
                ans[-1] = ''.join(list(reversed(ans[-1])))
                tmp = ans.pop()
                ans[-1] += tmp
            else:
                ans[-1] += i    
        return ans[0]           
        
        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
s = "(abcd)"
s = "(u(love)i)"
s = "a(bc)d"
s = "a(bcdefghijkl(mno)p)q"
ans = obj.reverseParentheses(s)
print(ans)

