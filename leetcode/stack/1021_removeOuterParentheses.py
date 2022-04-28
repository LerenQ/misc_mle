class Solution:

    def removeOuterParentheses(self, s:str) -> str:
        l = r = p = 0
        ans = ''
        for i, v in enumerate(s):
            if v == '(':
                l += 1
                if l == 1:
                    p = i
            if v == ')':
                r += 1
                if l == r:
                    ans += s[p+1:i]
                    l = r = 0
                    p = i+1

        return ans


test = Solution()
s = "(()())(())(()(()))"
ans = test.removeOuterParentheses(s)
print(ans)