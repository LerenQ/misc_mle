class Solution(object):

    def isPalindrome(self, x):
        """
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward.
        For example, 121 is palindrome while 123 is not.
        """
        if x < 0:
            return False
        xList = []
        indicator = 0
        integer = x
        while indicator == 0:
            remainder = integer % 10
            integer = integer // 10
            xList.append(remainder)
            if integer < 10:
                indicator = 1
                xList.append(integer)
        length = len(xList)
        for loc in range(length//2):
            if xList[loc] != xList[length - loc - 1]:
                return False
        return True


test = Solution()
p1 = test.isPalindrome(122221)
p2 = test.isPalindrome(-121)
p3 = test.isPalindrome(-1290)
p4 = test.isPalindrome(2**32)
print(p1)
