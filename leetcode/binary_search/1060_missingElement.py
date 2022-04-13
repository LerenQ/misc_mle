import collections
import string

class Solution:
    def missingElement(self, nums: 'list[int]', k: int) -> int:
        '''
        Given an integer array nums which is sorted in ascending order 
        and all of its elements are unique and given also an integer k, 
        return the kth missing number starting from the leftmost number of the array.

        '''
        if not nums or k == 0:
            return 0
        
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end
        

test = Solution()
nums = [4,7,9,10]
k = 1
ans = test.missingElement(nums, k)
print(ans)