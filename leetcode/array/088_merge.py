class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        You are given two integer arrays nums1 and nums2,
        sorted in non-decreasing order, and two integers m and n,
        representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        """
        counter1 = m - 1
        counter2 = n - 1
        counter3 = m + n - 1
        while counter3 >= 0:
            # print(counter3)
            if counter1 < 0:
                nums1[counter3] = nums2[counter2]
                counter2 -= 1
            elif counter2 < 0:
                nums1[counter3] = nums1[counter1]
                counter1 -= 1
            else:
                if nums1[counter1] >= nums2[counter2]:
                    nums1[counter3] = nums1[counter1]
                    counter1 -= 1
                else:
                    nums1[counter3] = nums2[counter2]
                    counter2 -= 1
            counter3 -= 1
        return nums1


test = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
p = test.merge(nums1, m, nums2, n)
print(p)
