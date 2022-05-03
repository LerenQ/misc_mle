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
        stack, d, ans, cur = [], [], '', ''
        for i in s:
            if i == '[':
                d.append(cur)
                cur = ''
                stack.append(ans)
                ans = ''
            elif i == ']':
                ans = stack.pop() + int(d.pop()) * ans
            elif i.isdigit():
                cur += i
            else:
                ans += i
        return ans

    

obj = Solution()
s = "3[a]23[bc]"
s = "3[a2[c]]2[bc]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
ans = obj.decodeString(s)
print(ans)

