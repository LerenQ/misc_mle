class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: 'list[str]') -> str:
        '''
        Given a string licensePlate and an array of strings words, 
        find the shortest completing word in words.

        A completing word is a word that contains all the letters in licensePlate. 
        Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. 
        If a letter appears more than once in licensePlate, 
        then it must appear in the word the same number of times or more.

        For example, if licensePlate = "aBc 12c", 
        then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
        Possible completing words are "abccdef", "caaacab", and "cbca".

        Return the shortest completing word in words. 
        It is guaranteed an answer exists. 
        If there are multiple shortest completing words, 
        return the first one that occurs in words.
        
        '''
        l = sorted(words, key=len)
        pstr = [i for i in licensePlate.lower() if i.isalpha()]
        # print(pstr)
        ans = ''
        for tmp in l:
            s = tmp
            flag = 1
            for i in pstr:
                if i in tmp:
                    tmp = tmp.replace(i, '', 1)
                else:
                    flag = 0
                    break
            if flag == 1:
                ans = s
                break
        return ans

        # method2: use counter making diff;

    
test = Solution()
licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
# words = ["looks","pest","stew","show"]
ans = test.shortestCompletingWord(licensePlate, words)
print(ans)