import collections
import heapq

class Solution:
    def countServers(self, grid: 'list[list[int]]') -> int:
        
        '''
        You are given a map of a server center, 
        represented as a m * n integer matrix grid, 
        where 1 means that on that cell there is a server and 0 means that it is no server. 
        Two servers are said to communicate if they are on the same row or on the same column.

        Return the number of servers that communicate with any other server.
        
        '''
        X, Y = tuple(map(sum, grid)), tuple(map(sum, zip(*grid)))
        return sum(X[i]+Y[j]>2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])

obj = Solution()
grid = [[1,0,0,0],[1,1,1,0],[0,0,1,0],[1,0,1,0]]
ans = obj.countServers(grid)
print(ans)