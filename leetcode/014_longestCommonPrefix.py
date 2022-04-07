class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string
        amongst an array of strings.
        If there is no common prefix, return an empty string "".
        """
        commonPrefix = []
        minlength = 200
        for i in strs:
            if len(i) < minlength:
                minlength = len(i)
        stop = 0
        for num in range(minlength):
            potential = strs[1][num]
            for s in strs:
                if potential == s[num]:
                    continue
                else:
                    stop = 1
            if stop == 1:
                break
            else:
                commonPrefix.append(potential)
        val = str()
        for i in commonPrefix:
            val += i
        if commonPrefix is None:
            return "There is no common prefix among the input strings."
        else:
            return val


test = Solution()
p1 = test.longestCommonPrefix(["flower", "flow", "flight"])
p2 = test.longestCommonPrefix(["dog", "racecar", "car"])
p3 = test.longestCommonPrefix(["dog", "docecar", "dar"])
print(p1)
