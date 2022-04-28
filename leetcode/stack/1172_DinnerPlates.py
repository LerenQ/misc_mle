from collections import deque

class DinnerPlates:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = deque()
        self.r = -1

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            sub = deque()
            sub.append(val)
            self.stack.append(sub)
            self.r += 1
        else:
            new = 1
            for k, v in enumerate(self.stack):
                if len(v) < self.capacity:
                    self.stack[k].append(val)
                    new = 0
                    break
            if new == 1:
                sub = deque()
                sub.append(val)
                self.stack.append(sub)
                self.r += 1
            

    def pop(self) -> int:
        while len(self.stack[self.r]) == 0:
            self.r -= 1
            if self.r == -1:
                return -1
        ans = self.stack[self.r].pop()
        return ans


    def popAtStack(self, index: int) -> int:
        if len(self.stack[index]) == 0:
            return -1
        else:
            ans = self.stack[index].pop()
        return ans



# Your DinnerPlates object will be instantiated and called as such:
capacity = 2
obj = DinnerPlates(capacity)

