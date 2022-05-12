
class Solution:
    def restoreIpAddresses(self, s: str) -> 'list[str]':
        '''
        A valid IP address consists of exactly four integers separated by single dots. 
        Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

            For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, 
            but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
        
        Given a string s containing only digits, 
        return all possible valid IP addresses that can be formed by inserting dots into s. 
        You are not allowed to reorder or remove any digits in s. 
        You may return the valid IP addresses in any order.
        
        '''
        ans, N = [], len(s)

        def backtrack(i, p):
            if i == N and len(p) == 4:
                ans.append('.'.join(p))
                return
            if len(p) > 4: return
            for j in range(1, 4):
                cur = s[i:i+j]
                if cur and (not cur.startswith('0') or cur =='0') and int(cur) < 256:
                    p.append(s[i:i+j])
                    backtrack(i+j, p)
                    p.pop()


        backtrack(0, [])
        return ans


obj = Solution()
s = "25525511135"
ans = obj.restoreIpAddresses(s)
print(ans)