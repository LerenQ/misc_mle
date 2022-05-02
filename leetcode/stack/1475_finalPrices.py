class Solution:
    def finalPrices(self, prices: 'list[int]') -> 'list[int]':
        '''
        Given the array prices where prices[i] is the price of the ith item in a shop. 
        There is a special discount for items in the shop, 
        if you buy the ith item, then you will receive a discount equivalent to prices[j] 
        where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, 
        you will not receive any discount at all.

        Return an array where the ith element is the final price you will pay for 
        the ith item of the shop considering the special discount.
        
        '''
        import copy
        p = copy.deepcopy(prices)
        for i in reversed(range(len(prices)-1)):
            for vj in p[i+1:]:
                if vj <= p[i]:
                    prices[i] -= vj
                    break
        return prices

    
    def finalPrices(self, prices: 'list[int]') -> 'list[int]':
        stack = []
        for i, a in enumerate(prices):
            while stack and prices[stack[-1]] > a:
                prices[stack.pop()] -= a
            stack.append(i)
        return prices

        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
arr = [3,1,2,4]
ans = obj.finalPrices(arr)
print(ans)

