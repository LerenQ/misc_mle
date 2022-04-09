class Solution:

    def getRow(self, rowIndex: int) -> 'list[int]':
        '''
        Given an integer rowIndex, 
        return the rowIndexth (0-indexed) row of the Pascal's triangle.
        In Pascal's triangle, 
        each number is the sum of the two numbers directly above it as shown:
        '''
        ans = [1]
        for _ in range(rowIndex):
            ans = [a+b for a, b in zip([0]+ans, ans+[0])]
        return ans


test = Solution()
rowIndex = 5
ans = test.getRow(rowIndex)
print(ans)