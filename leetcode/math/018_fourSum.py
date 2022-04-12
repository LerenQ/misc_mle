class Solution(object):

    def fourSum(self, nums, target):
        """
        Given an array nums of n integers, 
        return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
            0 <= a, b, c, d < n
            a, b, c, and d are distinct.
            nums[a] + nums[b] + nums[c] + nums[d] == target

        You may return the answer in any order.
        """
        def twoSum(ans:'list', res, lst, a1, a2):
            left = 0
            right = len(lst)-1
            while left < right:
                # print(left, right, a1, a2, lst,ans)
                tmp = lst[left] + lst[right]
                if tmp == res:
                    ans.append([a1, a2, lst[left], lst[right]])
                    left += 1
                    right -= 1
                    while lst[left] == lst[left-1] and left < right:
                        left += 1
                    while lst[right] == lst[right+1] and left < right:
                        right -= 1
                elif tmp < res:
                    left += 1
                else:
                    right -= 1

        nums.sort()
        lnt = len(nums)
        p1 = 0
        ans = []
        while p1 < lnt - 3:
            p2 = p1 + 1
            while p2 < lnt -2:
                res = target - nums[p1] - nums[p2]
                twoSum(ans, res, nums[p2+1:], nums[p1], nums[p2])
                p2 += 1
                while nums[p2] == nums[p2-1] and p2 < lnt -2:
                    p2 += 1
            p1 += 1
            while nums[p1] == nums[p1-1] and p1 < lnt - 3:
                p1 += 1
        return ans

        

test = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [0]
# nums = [0, 0, 0, 0]
# nums = [0, 0, 0]
nums = [-2,0,0,2,2]
nums = [1,0,-1,0,-2,2]
# nums = [-2,-1,0,0,1,2]
nums = [2,2,2,2,2]
p1 = test.fourSum(nums, 8)
print(p1)
