class Solution(object):

    def lengthOfLastWord(self, s):
        """
        Given a string s consisting of some words separated by some number of spaces,
        return the length of the last word in the string.
        A word is a maximal substring consisting of non-space characters only.
        """
        length = 0
        for i in reversed(range(len(s))):
            if s[i] == " " and length == 0:
                pass
            elif s[i] == " " and length != 0:
                break
            else:
                length += 1
        return length


test = Solution()
s = "Hello World"
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
p = test.lengthOfLastWord(s)
print(p)
