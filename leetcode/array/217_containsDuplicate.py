from collections import Counter

class Solution:

    def containsDuplicate(self, nums: 'list[int]') -> bool:
        '''
        Given an integer array nums, 
        return true if any value appears at least twice in the array, 
        and return false if every element is distinct.

        '''
        cnt = Counter(nums)

        return cnt.most_common(1)[0][1] > 1


test = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]
ans = test.containsDuplicate(nums)
print(ans)