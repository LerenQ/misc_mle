class Solution:
    def dailyTemperatures(self, temperatures: 'list[int]') -> 'list[int]':
        '''
        Given an array of integers temperatures represents the daily temperatures, 
        return an array answer such that answer[i] is the number of days 
        you have to wait after the ith day to get a warmer temperature. 
        If there is no future day for which this is possible, keep answer[i] == 0 instead.
        
        '''
        stack = []
        ans = [0]*len(temperatures)
        for i, a in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < a:
                s = stack.pop()
                ans[s] = i - s
            stack.append(i)
        return ans

        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
ans = obj.dailyTemperatures(temperatures)
print(ans)

