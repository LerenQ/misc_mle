class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        Given a balanced parentheses string s, return the score of the string.
        The score of a balanced parentheses string is based on the following rule:

            "()" has score 1.
            AB has score A + B, where A and B are balanced parentheses strings.
            (A) has score 2 * A, where A is a balanced parentheses string.
        
        '''
        
        res = l = 0
        for a, b in zip(s, s[1:]):
            if a + b == '()': res += 2 ** l
            l += 1 if a == '(' else -1
        return res
                
            
    

obj = Solution()
s = "(())()"
s = "(()(()))"
ans = obj.scoreOfParentheses(s)
print(ans)

