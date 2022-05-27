class Solution:
    def countSmaller(self, nums: 'list[int]') -> 'list[int]':
        '''
        You are given an integer array nums and you have to return a new counts array. 
        The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
        '''

        rst = [0] * len(nums)
        copy = [(nums[i], i) for i in range(len(nums))]
        
        def mergesort(ary, lp, rp):
            
            mp = (lp+rp) // 2
            if lp < rp - 1:
                mergesort(ary, lp, mp)
                mergesort(ary, mp, rp)
            
            # merge left and right
            tmp = ary[lp:rp]
            w = len(tmp)
            l, m = 0, w // 2
            for i in range(w):
                # print(ary, rst)
                if l== w // 2:
                    ary[lp+i] = tmp[m]
                    m += 1
                elif m == w:
                    rst[tmp[l][1]] += (m-w//2)
                    ary[lp+i] = tmp[l]
                    l += 1
                elif tmp[l][0] <= tmp[m][0]:
                    # print(tmp[l])
                    rst[tmp[l][1]] += (m-w//2)
                    ary[lp+i] = tmp[l]
                    l += 1
                else:
                    ary[lp+i] = tmp[m]
                    m += 1
        
        mergesort(copy, 0, len(nums))
        return rst