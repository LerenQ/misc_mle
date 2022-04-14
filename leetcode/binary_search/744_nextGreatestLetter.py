import collections
import string

class Solution:
    def nextGreatestLetter(self, letters: 'list[str]', target: str) -> str:
        '''
        Given a characters array letters that is sorted in non-decreasing order and a character target, 
        return the smallest character in the array that is larger than target.
        Note that the letters wrap around.
        For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
        
        '''
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1
        if letters[m] <= target:
            if m == len(letters) - 1:
                return letters[0]
            else:
                return letters[m+1]
        return letters[m]

        

test = Solution()
letters = ["c","f","j"]
target = "a"
target = "c"
target = "g"
target = "j"
ans = test.nextGreatestLetter(letters, target)
print(ans)