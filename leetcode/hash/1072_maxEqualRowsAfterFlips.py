import collections
import string

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: 'list[list[int]]') -> int:
        '''
        You are given an m x n binary matrix matrix.
        You can choose any number of columns in the matrix 
        and flip every cell in that column 
        (i.e., Change the value of the cell from 0 to 1 or vice versa).
        Return the maximum number of rows that have all values equal after some number of flips.

        '''
        
        c = collections.Counter()
        for row in matrix:
            c[tuple([x for x in row])] += 1
            c[tuple([1-x for x in row])] += 1
            print(c)
        return max(c.values())
        

test = Solution()
matrix = [[0,1],[1,0]]
ans = test.maxEqualRowsAfterFlips(matrix)
print(ans)