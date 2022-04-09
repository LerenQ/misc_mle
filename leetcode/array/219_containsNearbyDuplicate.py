class Solution:

    def containsNearbyDuplicate(self, nums: 'list[int]', k: int) -> bool:
        '''
        Given an integer array nums and an integer k, 
        return true if there are two distinct indices i and j in the array 
        such that nums[i] == nums[j] and abs(i - j) <= k.

        '''
        
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                if i - seen[val] <= k:
                    return True
            seen[val] = i
        return False


test = Solution()
nums = [1,0,1,1]
k = 1
ans = test.containsNearbyDuplicate(nums, k)
print(ans)