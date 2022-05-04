import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: 'list[int]', load: 'list[int]') -> 'list[int]':
        
        c, avl, nal = [0]*k, list(range(k)), []
        for i, (at,lt) in enumerate(zip(arrival, load)):
            
            while nal and nal[0][0] <= at:
                (_, server) = heapq.heappop(nal)
                bisect.insort(avl, server)
            if len(avl) == 0:
                continue

            loc = i % k
            # print(bisect.bisect_left(avl, loc), len(avl), avl, loc)
            index = bisect.bisect_left(avl, loc) % len(avl)
            server = avl.pop(index)
            c[server] += 1
            heapq.heappush(nal, (at+lt, server))

        maxcnt = max(c)
        return [i for i, v in enumerate(c) if v == maxcnt]
            

obj = Solution()
k = 3
arrival = [1,2,3,4,8,9,10]
load = [5,2,10,3,1,2,2]
ans = obj.busiestServers(k, arrival, load)
print(ans)

