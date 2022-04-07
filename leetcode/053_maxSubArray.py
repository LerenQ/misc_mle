class Solution(object):

    def strStr(self, nums):
        """
        Given an integer array nums,
        find the contiguous subarray
        (containing at least one number)
        which has the largest sum and return its sum.
        A subarray is a contiguous part of an array.

        Follow up: If you have figured out the O(n) solution,
        try coding another solution using the divide and conquer approach,
        which is more subtle.
        """
        maxsum = 0
        tmpsum = 0
        for i in range(len(nums)):
            if tmpsum + nums[i] <= 0:
                tmpsum = 0
            else:
                tmpsum += nums[i]
            if tmpsum > maxsum:
                maxsum = tmpsum
        return maxsum


test = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1]
nums = [5, 4, -1, 7, 8]
p = test.strStr(nums)
print(p)
