class Solution(object):

    def strStr(self, nums, target):
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.
        """
        # # O(n)
        # for i in range(len(nums)):
        #     # print(i)
        #     if nums[i] >= target:
        #         return i
        #     elif i == len(nums) - 1:
        #         return i+1
        # O(log n)
        head = 0
        tail = len(nums) - 1
        cuts = True
        length = tail - head + 1
        while cuts is True:
            # if only one component, then check if greater or less, then positioning.
            if head == tail:
                cuts = False
                if target <= nums[head]:
                    return head
                else:
                    return head + 1
            midloc = head + (length // 2)
            if nums[midloc] == target:
                return midloc
            elif nums[midloc] > target:
                tail = midloc
            else:
                head = midloc + 1
            length = tail - head + 1
            if length == 2:
                if nums[head] >= target:
                    return head
                else:
                    return head + 1


test = Solution()
nums = [1, 3, 5, 6]
target = 6
# nums = [1]
# target = 0
p = test.strStr(nums, target)
print(p)
