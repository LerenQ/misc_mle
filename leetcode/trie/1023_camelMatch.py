from typing import Pattern


class Solution:
    def camelMatch(self, queries: 'list[str]', pattern: str) -> 'list[bool]':
        '''
        Given an array of strings queries and a string pattern, return a boolean array answer
        where answer[i] is true if queries[i] matches pattern, and false otherwise.

        A query word queries[i] matches pattern if you can insert lowercase English letters pattern 
        so that it equals the query. 
        You may insert each character at any position and you may not insert any characters.

        '''
        def u(s):
            return [c for c in s if c.isupper()]

        def issub(s, t):
            it = iter(t)        # importand, pass the `Coop` testcase
            return all(c in it for c in pattern)
            
        return [u(q)==u(pattern) and issub(pattern, q) for q in queries]


obj = Solution()
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
ans = obj.camelMatch(queries, pattern)
print(ans)