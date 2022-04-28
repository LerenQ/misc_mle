from collections import deque
import heapq

class DinnerPlates:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = deque()
        self.q = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            sub = deque()
            sub.append(val)
            self.stack.append(sub)
        else:
            # print(self.stack, self.q)
            if self.q != [] and self.q[0] <= len(self.stack)-1:
                self.stack[self.q[0]].append(val)
                heapq.heappop(self.q)
            else:
                if len(self.stack[-1]) < self.capacity:
                    self.stack[-1].append(val)
                else:
                    sub = deque()
                    sub.append(val)
                    self.stack.append(sub)

    def pop(self) -> int:
        while self.stack:
            if len(self.stack[-1]) != 0:
                ans = self.stack[-1].pop()
                return ans
            else:
                self.stack.pop()
        return -1


    def popAtStack(self, index: int) -> int:
        if index > len(self.stack)-1:
            return -1
        if len(self.stack[index]) == 0:
            return -1
        else:
            ans = self.stack[index].pop()
            heapq.heappush(self.q, index)
        return ans



# Your DinnerPlates object will be instantiated and called as such:
capacity = 2
obj = DinnerPlates(capacity)

