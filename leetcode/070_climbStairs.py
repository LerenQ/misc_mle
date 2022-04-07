class Solution(object):

    def climbStairs(self, n):
        """
        You are climbing a staircase.
        It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps.
        In how many distinct ways can you climb to the top?
        """
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n in (0, 1, 2):
            return n
        fn2 = 1
        fn1 = 2
        for _ in range(n-2):
            fn = fn1 + fn2
            fn2 = fn1
            fn1 = fn
        return fn


test = Solution()
n = 44
p = test.climbStairs(n)
print(p)
