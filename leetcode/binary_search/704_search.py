import collections
import string

class Solution:
    def search(self, nums: 'list[int]', target: int) -> int:
        '''
        Given an array of integers nums which is sorted in ascending order, 
        and an integer target, write a function to search target in nums. 
        If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.

        '''
        idx = -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            idx = left 
        if nums[right] == target:
            idx = right

        return idx
        

test = Solution()
nums = [-1,0,3,5,9,12]
target = 9
ans = test.search(nums, target)
print(ans)