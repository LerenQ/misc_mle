class Solution:
    def replaceElements(self, arr: 'list[int]') -> 'list[int]':
        '''
        Given an array arr, 
        replace every element in that array with the greatest element 
        among the elements to its right, and replace the last element with -1.
        After doing so, return the array.
        
        '''
        m = 0
        ans = []
        for i in range(len(arr))[::-1]:
            if ans == []:
                ans.append(-1)
                m = arr[i]
            else:
                r = max(m, arr[i+1])
                ans.append(r)
                m = r
        return list(reversed(ans))
        
# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
arr = [3,1,2,4]
ans = obj.replaceElements(arr)
print(ans)

