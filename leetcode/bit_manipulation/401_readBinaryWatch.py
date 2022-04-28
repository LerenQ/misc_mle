from itertools import combinations

class Solution:
    def readBinaryWatch1(self, turnedOn: int) -> 'list[str]':
        '''
        A binary watch has 4 LEDs on the top which represent the hours (0-11), 
        and the 6 LEDs on the bottom represent the minutes (0-59). 
        Each LED represents a zero or one, with the least significant bit on the right.

        '''       
        hours = list(map(lambda x: x*60, (1, 2, 4, 8)))
        minutes = [32, 16, 8, 4, 2, 1]
        #tbd

    
    def readBinaryWatch2(self, turnedOn: int) -> 'list[str]':
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    ans.append(f'{h}:{m:02d}')
        return ans


test = Solution()
turnedOn = 1
ans = test.readBinaryWatch2(turnedOn)
print(ans)