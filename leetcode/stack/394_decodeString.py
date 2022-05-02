class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Given an encoded string, return its decoded string.
        The encoding rule is: k[encoded_string], 
        where the encoded_string inside the square brackets is being repeated exactly k times. 
        Note that k is guaranteed to be a positive integer.

        You may assume that the input string is always valid; 
        there are no extra white spaces, 
        square brackets are well-formed, etc.

        Furthermore, you may assume that the original data does not contain any digits and that
        digits are only for those repeat numbers, k. 
        For example, there will not be input like 3a or 2[4].
        
        '''
        ans = ''
        pstack, d, c = [], [], []
        for i in s:
            if i.isdigit():
                if i.d[-1]
                    d[-1] += i
            elif i == '[':
                pstack.append(i)
            elif i == ']':
                pstack.pop()
                tmp = int(d[-1])*str(c[-1])
                d.pop()
                c.pop()
                if c:
                    c[-1] += tmp
                else:
                    ans += tmp
            else:


        return ans

    

obj = Solution()
s = "3[a]23[bc]"
s = "3[a2[c]]2[bc]"
ans = obj.decodeString(s)
print(ans)

