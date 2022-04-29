class Solution:
    '''
    Given an array of integers arr, find the sum of min(b), 
    where b ranges over every (contiguous) subarray of arr. 
    Since the answer may be large, return the answer modulo 109 + 7.
    '''
    def sumSubarrayMins(self, arr: 'list[int]') -> int:
        
        n, mod = len(arr), 10**9+7

        l, r, s1, s2 = [0]*n, [0]*n, [], []
        for i in range(n):
            cnt = 1
            while s1 and s1[-1][0] >= arr[i]: cnt += s1.pop()[1]
            l[i] = cnt
            s1.append((arr[i],cnt))
        for i in range(n)[::-1]:
            cnt = 1
            while s2 and s2[-1][0] > arr[i]: cnt += s2.pop()[1]
            r[i] = cnt
            s2.append((arr[i], cnt))

        return sum(i*j*k for i, j, k in zip(arr, l, r)) % mod

# Your StockSpanner object will be instantiated and called as such:
obj = Solution()
arr = [3,1,2,4]
ans = obj.sumSubarrayMins(arr)
print(ans)

