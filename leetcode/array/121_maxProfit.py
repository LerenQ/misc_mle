class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         heap = [(prices[0], 0)]

#         for i in prices:
#             # print(heap)
#             if i <= heap[0][0] and heap[0][1] == 0:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, (i, 0))
            
#             elif i <= heap[0][0] and heap[0][1] > 0:
#                 heapq.heappush(heap, (i, 0))
                
#             elif i > heap[0][0]:
#                 t, v = heap[0][0], max(i - heap[0][0], heap[0][1])
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, (t, v))
                
#         return max([heap[i][1] for i in range(len(heap))])
                
    def maxProfit(self, prices: 'list[int]') -> int:
        mval = prices[0]
        recd = 0
        for i in prices[1:]:
            if i < mval:
                mval = i
            elif i-mval > recd:
                recd = i-mval
        return recd

