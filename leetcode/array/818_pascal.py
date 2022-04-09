class Solution:

    def generate(self, numRows: int) -> 'list[list[int]]':
        ans = [[1]]
        cnt = 1
        cur = [0, 1, 0]
        while cnt < numRows:
            layer = []
            for i in range(len(cur)-1):
                layer.append(cur[i] + cur[i+1])
            ans.append(layer)
            cnt += 1
            cur = [0] + layer + [0]
        return ans


test = Solution()
numRows = 5
ans = test.generate(numRows)
print(ans)