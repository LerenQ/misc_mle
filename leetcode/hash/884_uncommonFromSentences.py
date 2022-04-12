import collections
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> 'list[str]':
        '''
        A sentence is a string of single-space separated words 
        where each word consists only of lowercase letters.
        A word is uncommon if it appears exactly once in one of the sentences, 
        and does not appear in the other sentence.

        Given two sentences s1 and s2, 
        return a list of all the uncommon words. You may return the answer in any order. 
        
        '''
        l1 = collections.Counter(s1.split(' '))
        l2 = collections.Counter(s2.split(' '))
        t = l1 + l2
        ans = []
        for i in t:
            if t[i] < 2:
                ans.append(i)
        return ans
        

test = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
ans = test.uncommonFromSentences(s1, s2)
print(ans)