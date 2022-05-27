class Solution:
    def countRangeSum(self, nums: 'list[int]', lower: int, upper: int) -> int:
        
        self.rst, self.lower, self.upper = 0, lower, upper
        presum = self.presums(nums)
        # print(presum)
        self.temp = [None for _ in presum]
        self.sort(presum, 0, len(presum))
        return self.rst
    
    
    def presums(self, nums):
        presum = [0] * len(nums)
        presum[0] = nums[0]
        for k, i in enumerate(nums[1:]):
            presum[k+1] = i + presum[k]
        return [0] + presum
        
        
    def sort(self, ary, l, r):
        if l < r -1:
            m = (l + r) // 2
            self.sort(ary, l, m)
            self.sort(ary, m, r)
            self.merge(ary, l, m, r)
    
    
    def merge(self, ary, l, m, r):
        mid, lan = m, r - l
        
        for i in range(l, r):
            self.temp[i] = ary[i]
            
#         # check if meet condition, time limit exceeded;
#         for i in range(l, mid):
#             for j in range(m, r):
#                 if self.lower <= self.temp[j] - self.temp[i] <= self.upper:
#                     self.rst += 1
        
        # like sliding window
        s, e = mid, mid
        for i in range(l,mid):
            while s < r and self.temp[s] - self.temp[i] < self.lower:
                s += 1
            while e < r and self.temp[e] - self.temp[i] <= self.upper:
                e += 1
            self.rst += e-s
        
        for i in range(l, r):
            if l == mid:
                ary[i] = self.temp[m]
                m += 1
            elif m == r:
                ary[i] = self.temp[l]
                l += 1
            elif self.temp[l] < self.temp[m]:
                ary[i] = self.temp[l]
                l += 1
            else:
                ary[i] = self.temp[m]
                m += 1




    def countRangeSum2(self, nums: 'list[int]', lower: int, upper: int) -> int:
        # brute force:
        rst = 0
        presum = [0] * len(nums)
        presum[0] = nums[0]
        for k, i in enumerate(nums[1:]):
            presum[k+1] = i + presum[k]
        presum = [0] + presum
        # print(presum)
        
        for i in nums:
            if lower <= i <= upper:
                rst += 1
        
        p = 2
        while p < len(presum):
            q = 0
            while q < p-1:
                if lower <= (presum[p] - presum[q]) <= upper:
                    # print(p, q)
                    rst += 1
                q += 1
            p += 1
        # print(rst)
        return rst