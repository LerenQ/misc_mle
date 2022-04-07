class Solution(object):

    def strStr(self, haystack, needle):
        """
        Implement strStr().
        Return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        Clarification:
        What should we return when needle is an empty string?
        This is a great question to ask during an interview.
        For the purpose of this problem,
        we will return 0 when needle is an empty string.
        This is consistent to C's strstr() and Java's indexOf().
        """
        if len(needle) == 0:
            return 0
        indexStr = -1
        for i in range(len(haystack)):
            # print(indexStr)
            for j in range(min(len(needle), len(haystack)-i)):
                if needle[j] != haystack[i+j]:
                    break
                if j == len(needle) - 1:
                    indexStr = i
            if indexStr > 0:
                break
        return indexStr


test = Solution()
haystack = "hello"
needle = "ll"
haystack = "aaaaa"
needle = "bbb"
haystack = "lerenqenn"
needle = "en"
p = test.strStr(haystack, needle)
print(p)
