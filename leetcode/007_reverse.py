class Solution(object):

    def reverse(self, x):
        """
        Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside the signed 32-bit integer
        range [-2^31, 2^31 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers
        (signed or unsigned).
        """
        sign = 1
        if x > 2**31 - 1 or x < -2**31:
            return 0
        if x < 0:
            sign = -1
            x = -x
        xList = []
        indicator = 0
        integer = x
        val = 0
        while indicator == 0:
            remainder = integer % 10
            integer = integer // 10
            xList.append(remainder)
            if integer < 10:
                indicator = 1
                xList.append(integer)
        for loc in range(len(xList)):
            val += xList[loc] * (10 ** (len(xList) - loc - 1))
        return val * sign


test = Solution()
p1 = test.reverse(123)
p2 = test.reverse(120)
p3 = test.reverse(-1290)
p4 = test.reverse(2**32)
print(p3)
