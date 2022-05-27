from collections import heapq

class Solution:
    def sortArray(self, nums: 'list[int]') -> 'list[int]':
        def sort(nums):

            n = len(nums)
            if n == 1:
                return nums
            ind = n // 2
            l = sort(nums[:ind])
            r = sort(nums[ind:])
            
            rst = []
            while (l!=[] and r!=[]):
                if l[0] < r[0]:
                    rst.append(heapq.heappop(l))
                else:
                    rst.append(heapq.heappop(r))
            tmp = l+r
            while tmp != []:
                rst.append(heapq.heappop(tmp))
            
            return rst
        
        return sort(nums)
        