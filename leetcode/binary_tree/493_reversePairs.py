from collections import heapq

class Solution:
    def reversePairs(self, nums: 'list[int]') -> int:
        self.rst = 0
        self.mergeSort(nums, 0, len(nums))
        return self.rst
        
    def merge(self, ary, l, r):
        temp = ary[l:r]
        lp, mr, mp, leng = 0, len(temp)//2, len(temp)//2, len(temp)

        # check if meet condition
        while lp < mr:
            while mp < leng and temp[lp] > 2*temp[mp]:
                mp += 1
            self.rst += mp - mr
            lp += 1
        
        lp, mp = 0, len(temp) //2
        
        for i in range(leng):
            if lp == mr:
                ary[l+i] = temp[mp]
                mp += 1
            elif mp == leng:
                ary[l+i] = temp[lp]
                lp += 1
            elif temp[lp] < temp[mp]:
                ary[l+i] = temp[lp]
                lp += 1
            else:
                ary[l+i] = temp[mp]
                mp += 1

                
    def mergeSort(self, ary, l, r):

        if l < r - 1:
            m = (l+r)//2
            self.mergeSort(ary, l, m)
            self.mergeSort(ary, m, r)
            self.merge(ary, l, r)
        