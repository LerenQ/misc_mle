from bisect import bisect_left 


class Solution:
    def findMin(self, nums: 'list[int]') -> int:
        '''
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
        For example, the array nums = [0,1,2,4,5,6,7] might become:

            [4,5,6,7,0,1,2] if it was rotated 4 times.
            [0,1,2,4,5,6,7] if it was rotated 7 times.
            [1,2,4,5,6,7,0]
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
        1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, 
        return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] <= nums[right]) and (nums[left] <= nums[mid]):
                return nums[left]
            if (nums[mid] <= nums[right]) and (nums[left] >= nums[mid]):
                right = mid
            if (nums[mid] >= nums[right]) and (nums[left] <= nums[mid]):
                left = mid + 1
        

test = Solution()
nums = [3,4,5,1,2]
ans = test.findMin(nums)
print(ans)