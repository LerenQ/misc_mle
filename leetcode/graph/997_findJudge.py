from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: 'list[list[int]]') -> int:
        '''
        In a town, there are n people labeled from 1 to n. 
        There is a rumor that one of these people is secretly the town judge.


        '''
        if not trust and n == 1:
            return -1
            
        frm = defaultdict(lambda: [])
        til = defaultdict(lambda: [])
        cnt = []
        for _, (x, y) in enumerate(trust):
            frm[x] += [y]
            til[y] += [x]
        # print(frm, til)
        for k, v in til.items():
            if len(v) == n-1 and (k not in frm.keys()):
                cnt.append(k)
        if len(cnt) == 1:
            return cnt[0]
        else:
            return -1


obj = Solution()
n = 3
n = 2
trust = [[1,3],[2,3],[3,1]]
trust = [[1,2]]
ans = obj.findJudge(n, trust)
print(ans)