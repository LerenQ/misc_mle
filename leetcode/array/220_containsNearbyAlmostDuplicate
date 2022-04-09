from collections import OrderedDict

class Solution:

    def containsNearbyAlmostDuplicate(self, nums: 'list[int]', k: int, t: int) -> bool:
        '''
        Given an integer array nums and two integers k and t, 
        return true if there are two distinct indices i and j in the array 
        such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

        '''
        if k < 1 or t < 0:
            return False
        dic = OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key-1), dic.get(key), dic.get(key+1)):
                if m is not None and abs(m-n) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False


test = Solution()
nums = [100,2,30,1]
k = 3
t = 2
ans = test.containsNearbyAlmostDuplicate(nums, k, t)
print(ans)