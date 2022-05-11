import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: 'list[int]', nums2: 'list[int]') -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        med = (l1+l2) // 2
        
        cnt = 0
        rec = None
        
        while cnt < med:
            n1 = nums1[0] if nums1 else float('inf')
            n2 = nums2[0] if nums2 else float('inf')
            if n1 < n2:
                rec = heapq.heappop(nums1)
            else:
                rec = heapq.heappop(nums2)
            cnt += 1
        
        n1 = nums1[0] if nums1 else float('inf')
        n2 = nums2[0] if nums2 else float('inf')

        if (l1 + l2) % 2 != 0:
            return min(n1, n2)
        else:
            if n1 < n2:
                k1 = n1
                heapq.heappop(nums1)
            else:
                k1 = n2
                heapq.heappop(nums2)
            
            return (rec + k1)/2

