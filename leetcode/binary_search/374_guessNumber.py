# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        We are playing the Guess Game. The game is as follows:
        I pick a number from 1 to n. You have to guess which number I picked.
        Every time you guess wrong, 
        I will tell you whether the number I picked is higher or lower than your guess.

        You call a pre-defined API int guess(int num), which returns three possible results:
            -1: Your guess is higher than the number I picked (i.e. num > pick).
            1: Your guess is lower than the number I picked (i.e. num < pick).
            0: your guess is equal to the number I picked (i.e. num == pick).
        
        Return the number that I picked.
        
        '''
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1

test = Solution()
n = 10
ans = test.guessNumber(n)
print(ans)