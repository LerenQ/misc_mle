class Solution(object):

    def isValid(self, s):
        """
        Valid Parentheses
        Given a string s containing just the characters
        '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
            An input string is valid if:
            1. Open brackets must be closed by the same type of brackets.
            2. Open brackets must be closed in the correct order.
        """
        pair = {'(': ')', '{': '}', '[': ']'}
        right = [')', '}', ']']
        collect = []
        tmp = []
        for i in range(len(s)):
            collect.append(s[i])
        for i in collect:
            tmp.append(i)
            if i in right and i == pair[tmp[-2]]:
                tmp.pop(-1)
                tmp.pop(-1)
            elif i in right and i != pair[tmp[-2]]:
                return False
            else:
                # the case when i in left
                continue
        if len(tmp) == 0:
            return True
        else:
            return False


test = Solution()
p0 = test.isValid("()")
p1 = test.isValid("()[]{}")
p2 = test.isValid("(]")
p3 = test.isValid("([)]")
p4 = test.isValid("{[]}")
print(p4)
