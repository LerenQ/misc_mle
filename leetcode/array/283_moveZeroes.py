class Solution:
    def moveZeroes(self, nums: 'list[int]') -> None:
        '''
        Given an integer array nums, 
        move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
        '''
        n = len(nums)       
        left = 0
        right = 0
        while right <= n - 1:
            while right < n and nums[right] == 0:
                right += 1
            if right == n:
                break
            nums[left] = nums[right]
            left += 1
            right += 1
        for i in range(left, n):
            nums[i] = 0
            

test = Solution()
nums = [0,1,0,3,12]
nums = [1]
nums = [1, 0]
nums = [2, 1]
test.moveZeroes(nums)
print(nums)
