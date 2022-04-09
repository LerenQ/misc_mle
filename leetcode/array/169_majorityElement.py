from collections import Counter


class Solution:

    def majorityElement(self, nums: 'list[int]') -> 'list[int]':
        '''
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.

        '''
        ctr = Counter(nums)
        # print(ctr.items())
        # print(len(nums)/3)
        return ctr.most_common(1)[0][0]


test = Solution()
nums = [4,2,5,6,6]
ans = test.majorityElement(nums)
print(ans)