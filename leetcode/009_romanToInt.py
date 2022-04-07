class Solution(object):

    def romanToInt(self, s):
        """
        Roman numerals are represented by seven different symbols:
        I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral,
        just two one's added together.
        12 is written as XII, which is simply X + II.
        The number 27 is written as XXVII, which is XX + V + II.
        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead,
        the number four is written as IV.
        Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX.
        There are six instances where subtraction is used:
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.
        """
        xList = []
        for tmp in range(len(s)):
            xList.append(s[tmp])
        romandict = {}
        romandict["I"] = 1
        romandict["V"] = 5
        romandict["X"] = 10
        romandict["L"] = 50
        romandict["C"] = 100
        romandict["D"] = 500
        romandict["M"] = 1000
        romandict["Z"] = 0
        val = 0
        for tmp in range(len(xList)-1):
            if xList[tmp] == "I" and xList[tmp+1] == "V":
                val += 4
                xList[tmp+1] = "Z"
            elif xList[tmp] == "I" and xList[tmp+1] == "X":
                val += 9
                xList[tmp+1] = "Z"
            elif xList[tmp] == "X" and xList[tmp+1] == "L":
                val += 50
                xList[tmp+1] = "Z"
            elif xList[tmp] == "X" and xList[tmp+1] == "C":
                val += 90
                xList[tmp+1] = "Z"
            elif xList[tmp] == "C" and xList[tmp+1] == "D":
                val += 400
                xList[tmp+1] = "Z"
            elif xList[tmp] == "C" and xList[tmp+1] == "M":
                val += 900
                xList[tmp+1] = "Z"
            else:
                val += romandict[xList[tmp]]
        val += romandict[xList[-1]]
        return val


test = Solution()
p1 = test.romanToInt("III")
p2 = test.romanToInt("IV")
p3 = test.romanToInt("IX")
p4 = test.romanToInt("LVIII")
p5 = test.romanToInt("MCMXCIV")
print(p5)
