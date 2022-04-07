class Solution(object):

    def mySqrt(self, x):
        """
        Given a non-negative integer x,
        compute and return the square root of x.
        Since the return type is an integer,
        the decimal digits are truncated,
        and only the integer part of the result is returned.
        Note: You are not allowed to use any built-in exponent
        function or operator, such as pow(x, 0.5) or x ** 0.5.
        """
        # counter = 0
        # while True:
        #     # print(counter)
        #     if counter * counter > x:
        #         return counter - 1
        #     else:
        #         counter += 1
        # binary search
        if x == 0 or x == 1:
            return x
        counter = x / 2
        upper = x
        lower = 0
        while True:
            print(upper, lower, counter)
            if counter * counter > x:
                upper = counter
                counter = upper - (upper - lower) / 2
            elif counter * counter < x:
                lower = counter
                counter = (upper - lower) / 2 + lower
            else:
                return int(counter)
            if upper - lower < 1:
                if (upper // 1) * (upper // 1) <= x:
                    return int(upper)
                else:
                    return int(lower)


test = Solution()
x = 4
x = 44944
x = 8
p = test.mySqrt(x)
print(p)
