from collections import deque
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        You are given a string s and an integer k, 
        a k duplicate removal consists of choosing k adjacent 
        and equal letters from s and removing them, 
        causing the left and the right side of the deleted substring to concatenate together.
        We repeatedly make k duplicate removals on s until we no longer can.
        Return the final string after all such duplicate removals have been made. 
        It is guaranteed that the answer is unique.
        
        '''
        ans = deque([])
        for i in s:
            cnt = 1 if len(ans) == 0 or i != ans[-1][0] else ans[-1][1]+1
            if cnt == 1:
                ans.append((i,1))
            elif cnt < k:
                ans.pop()
                ans.append((i, cnt))
            else:
                ans.pop()

        f = ''
        for i in ans:
            f += i[0] * i[1]
        return f
            
        
        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
s = "abcd"
k = 2
s = "deeedbbcccbdaa"
k = 3
ans = obj.removeDuplicates(s, k)
print(ans)

