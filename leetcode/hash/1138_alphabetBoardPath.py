import collections
import string

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        '''
        On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
        Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"],
        Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  
        You may return any path that does so.
        '''
        m = {k: (i//5, i%5) for i, k in enumerate(string.ascii_lowercase)}
        x0 = y0 = 0
        ans = ''
        for i in target:
            x, y = m[i]
            if y0 > y: ans += 'L'*(y0-y)
            if x0 > x: ans += 'U'*(x0-x)
            if y0 < y: ans += 'R'*(y-y0)
            if x0 < x: ans += 'D'*(x-x0)           
            x0, y0 = x, y
            ans += '!'
        return ans
        

test = Solution()
target = "leet"
ans = test.alphabetBoardPath(target)
print(ans)