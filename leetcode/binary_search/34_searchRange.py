from bisect import bisect_left 


class Solution:
    def searchRange(self, nums: 'list[int]', target: int) -> 'list[int]':
        '''
        Given an array of integers nums sorted in non-decreasing order, 
        find the starting and ending position of a given target value.
        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.

        '''

        l, r = 0, len(nums) - 1
        ans = [-1, -1]
        mid = 0
        while l <= r and nums[mid] != target:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1

        if nums != [] and (nums[mid] == target):
            lend = rend = mid
            while l <= lend:
                lmid = (l + lend) // 2
                if nums[lmid] != target:
                    l = lmid + 1
                else:
                    lend = lmid - 1
            while rend <= r:
                rmid = (r + rend) // 2
                if nums[rmid] != target:
                    r = rmid - 1
                else:
                    rend = rmid + 1
            ans = [l, r]
        return ans
        

test = Solution()
nums = [5,8,8,8,8,10]
nums = []
target = 8
target = 0
ans = test.searchRange(nums, target)
print(ans)