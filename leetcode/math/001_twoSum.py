class Solution(object):

    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rList = []
        for loc_x in range(0, len(nums)):
            remain = target - nums[loc_x]
            for loc_y in range(0, len(nums)):
                if (remain == nums[loc_y]) and (loc_y != loc_x):
                    rList = [loc_x, loc_y]
                    return rList
        if rList is None:
            print("no match")
        return rList


test = Solution()
p1 = test.twoSum([2, 7, 11, 15], 9)
p2 = test.twoSum([3, 2, 4], 6)
p3 = test.twoSum([3, 3], 6)
print(p3)
