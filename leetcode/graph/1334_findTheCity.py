import collections
import heapq

class Solution:
    def findTheCity(self, n: int, edges: 'list[list[int]]', distanceThreshold: int) -> int:
        
        '''
        There are n cities numbered from 0 to n-1. 
        Given the array edges where edges[i] = [fromi, toi, weighti] 
        represents a bidirectional and weighted edge between cities fromi and toi, 
        and given the integer distanceThreshold.        

        Return the city with the smallest number of cities 
        that are reachable through some path and whose distance is at most distanceThreshold, 
        If there are multiple such cities, return the city with the greatest number. 
        
        '''
        g = collections.defaultdict(list)
        for i, j, l in edges:
            g[i].append((j, l))
            g[j].append((i, l))

        def dijkstra(city):
            heap = [(0, city)]
            mark = {}

            while heap:
                d, cur = heapq.heappop(heap)
                if cur in mark:
                    continue
                if cur != city:
                    mark[cur] = d
                for t, l in g[cur]:
                    if t in mark:
                        continue
                    if l + d <= distanceThreshold:
                        heapq.heappush(heap, (l+d, t))
            return len(mark)

        return min(range(n), key = lambda x: (dijkstra(x), -x))


obj = Solution()
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
ans = obj.findTheCity(n, edges, distanceThreshold)
print(ans)