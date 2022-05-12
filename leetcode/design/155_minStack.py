class MinStack:
    '''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.

    '''

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.m) == 0:
            self.m.append(val)
        else:
            if val < self.m[-1]:
                self.m.append(val)
            else:
                self.m.append(self.m[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()

    def top(self) -> int:
        return int(self.stack[-1])

    def getMin(self) -> int:
        return int(self.m[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()