class Solution(object):

    def addBinary(self, a, b):
        """
        Given two binary strings a and b, return their sum as a binary string.
        """
        increase = 0
        stop = 0
        c = str()
        while stop == 0:
            print(a, b, c, increase)
            if a[-1] == "0" and b[-1] == "0":
                if increase == 0:
                    c = "0" + c
                else:
                    c = "1" + c
                    increase = 0
            elif a[-1] == "1" and b[-1] == "1":
                if increase == 0:
                    c = "0" + c
                    increase = 1
                else:
                    c = "1" + c
            else:
                if increase == 0:
                    c = "1" + c
                else:
                    c = "0" + c
            a = a[0:-1]
            b = b[0:-1]
            if len(a) == 0 and len(b) != 0:
                a = "0"
            elif len(a) != 0 and len(b) == 0:
                b = "0"
            elif len(a) == 0 and len(b) == 0:
                stop = 1
                if increase == 1:
                    c = "1" + c
        return c


test = Solution()
a = "11"
b = "1"
a = "1010"
b = "1011"
p = test.addBinary(a, b)
print(p)
