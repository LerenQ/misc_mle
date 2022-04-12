class Solution:
    def longestWord(self, words: 'list[str]') -> str:
        '''
        Given an array of strings words representing an English Dictionary, 
        return the longest word in words that can be built one character at a time by other words in words.

        If there is more than one possible answer, 
        return the longest word with the smallest lexicographical order. 
        If there is no answer, return the empty string.
        
        '''
        
        l = sorted(sorted(words), key=len)
        # print(l)
        dic = set()
        ans = ''
        for i in range(len(l)):
            if l[i][:-1] in dic and len(l[i])>len(ans):
                ans = l[i]
            dic.add(l[i])
        return ans

    
test = Solution()
# words = ["w","wo","wor","worl","world"]
# words = ["a","banana","app","appl","ap","apply","apple"]
words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
ans = test.longestWord(words)
print(ans)