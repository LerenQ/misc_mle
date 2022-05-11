import operator
from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: 'list[list[int]]') -> bool:
        '''
        We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
        Each person may dislike some other people, 
        and they should not go into the same group.

        Given the integer n and the array dislikes where dislikes[i] = [ai, bi] 
        indicates that the person labeled ai does not like the person labeled bi, 
        return true if it is possible to split everyone into two groups in this way.


        '''
        g = defaultdict(list)
        for x, y in dislikes:
            g[x].append(y)
            g[y].append(x)

        mark = {}
        def dfs(node, c=0):
            if node in mark:
                return mark[node] == c
            mark[node] = c
            return all(dfs(n, c^1) for n in g[node])

        return all(dfs(n) for n in range(1,n+1) if n not in mark)


obj = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
ans = obj.possibleBipartition(n, dislikes)
print(ans)