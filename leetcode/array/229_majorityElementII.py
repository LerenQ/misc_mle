from collections import Counter


class Solution:

    def majorityElement(self, nums: 'list[int]') -> 'list[int]':
        '''
        Given an integer array of size n, 
        find all elements that appear more than ⌊ n/3 ⌋ times.

        '''
        ctr = Counter(nums)
        # print(ctr.items())
        # print(len(nums)/3)
        return [k for k, v in ctr.items() if v > len(nums)/3]


test = Solution()
nums = [4,2,5,6,6]
ans = test.majorityElement(nums)
print(ans)