class Solution:
    def maxScoreSightseeingPair(self, values: 'list[int]') -> int:
        '''
        You are given an integer array values where values[i] 
        represents the value of the ith sightseeing spot. 
        Two sightseeing spots i and j have a distance j - i between them.
        The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: 
        the sum of the values of the sightseeing spots, 
        minus the distance between them.

        Return the maximum score of a pair of sightseeing spots.
        
        '''
        first = []
        second = []
 
        for i, a in enumerate(values):
            first.append(a + i)
            second.append(a - i)
 
        for i in reversed(range(len(first)-1)):
            second[i] = max(second[i+1], second[i])
 
        best = 0
        for i in range(len(values)-1):
            best = max(best, first[i] + second[i+1])
 
        return best
        

test = Solution()
values = [8,1,5,2,6]
ans = test.maxScoreSightseeingPair(values)
print(ans)