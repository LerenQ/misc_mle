class Solution(object):

    def removeElement(self, nums, val):
        """
        Given an integer array nums and an integer val,
        remove all occurrences of val in nums in-place.
        The relative order of the elements may be changed.

        Since it is impossible to change the length of the array
        in some languages, you must instead have the result be placed
        in the first part of the array nums. More formally,
        if there are k elements after removing the duplicates,
        then the first k elements of nums should hold the final result.
        It does not matter what you leave beyond the first k elements.

        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array.
        You must do this by modifying the input array in-place with O(1) extra memory.
        """
        counter = 0
        if nums is None:
            return 0, []
        for i in range(0, len(nums)):
            # print(i, nums)
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter, nums


test = Solution()
# nums = [3, 2, 2, 3]
nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 3
val = 2
p = test.removeElement(nums, val)
print(p)
