class Solution(object):

    def threeSum(self, nums):
        """
        Given an integer array nums, 
        return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, 
        and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # to avoid duplication in the final list
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums[i+1:], -nums[i], ans)
        return ans

    def twoSum(self, nums, target, ans):
        low = 0
        high = len(nums) -1
        while low < high:
            sums = nums[low] + nums[high]
            if sums < target:
                low += 1
            elif sums > target:
                high -= 1
            else:
                ans.append([-target, nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
     

test = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0]
# nums = [0, 0, 0, 0]
# nums = [0, 0, 0]
nums = [-2,0,0,2,2]
p1 = test.threeSum(nums)
print(p1)
