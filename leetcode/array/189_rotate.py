class Solution:

    def rotate(self, nums: 'list[int]', k: int) -> None:
        '''
        Given an array, rotate the array to the right by k steps, where k is non-negative.

        '''

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[0:-k]


test  = Solution()
nums = [1,2]
k = 3
test.rotate(nums, k)
print(nums)