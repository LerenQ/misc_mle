from collections import Counter
class Solution(object):

    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        '''
        Given four integer arrays nums1, nums2, nums3, and nums4 
        all of length n, return the number of tuples (i, j, k, l) such that:

        0 <= i, j, k, l < n
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

        '''
        ab = Counter(-a-b for a in nums1 for b in nums2)
        return sum(ab[c+d] for c in nums3 for d in nums4)

test = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0]
# nums = [0, 0, 0, 0]
# nums = [0, 0, 0]
nums = [-2,0,0,2,2]
nums = [1,0,-1,0,-2,2]
# nums = [-2,-1,0,0,1,2]
# nums = [2,2,2,2,2]
p1 = test.fourSumCount(nums, nums, nums, nums)
print(p1)
