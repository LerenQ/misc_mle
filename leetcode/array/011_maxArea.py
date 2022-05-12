class Solution:
    def maxArea(self, height: 'list[int]') -> int:
        l = 0
        r = len(height) - 1
        sq = 0
        while l != r:
            sq = max(sq, (r-l) * min(height[l], height[r]))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return sq