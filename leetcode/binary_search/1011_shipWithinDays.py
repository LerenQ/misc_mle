class Solution:
    def shipWithinDays(self, weights: 'list[int]', days: int) -> int:
        '''
        A conveyor belt has packages that must be shipped from one port to another within days days.
        The ith package on the conveyor belt has a weight of weights[i]. 
        Each day, we load the ship with packages on the conveyor belt 
        (in the order given by weights). 
        We may not load more weight than the maximum weight capacity of the ship.

        Return the least weight capacity of the ship 
        that will result in all the packages on the conveyor belt being shipped within days days.
        
        '''
        def can_ship(days, cap):
            w = 0
            d = 1
            for i in weights:
                if w + i <= cap:
                    w += i
                else:
                    w = i
                    d += 1
                if d > days:
                    return False
            return True

        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_ship(days, mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


test = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
ans = test.shipWithinDays(weights, days)
print(ans)