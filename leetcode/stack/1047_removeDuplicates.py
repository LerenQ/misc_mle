class Solution:

    def removeDuplicates(self, s: str) -> str:
        '''
        You are given a string s consisting of lowercase English letters. 
        A duplicate removal consists of choosing two adjacent and equal letters and removing them.
        
        '''

        ans = ' '
        for i in s:
            if ans[-1] == i:
                ans = ans[:-1]
            else:
                ans += i
        
        return ans[1:]

    def removeDuplicates2(self, s: str) -> str:
        from collections import deque
        ans = deque()
        for i in s:
            if len(ans) == 0:
                ans.append(i)
            elif ans[-1] != i:
                ans.append(i)
            else:
                ans.pop()

        return ''.join(ans)



test = Solution()
s = "abbaca"
ans = test.removeDuplicates2(s)
print(ans)