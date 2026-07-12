class MinStack(object):

    def __init__(self):
        self.stk = []
        self.stk_min = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.stk_min:
            val = min(val, self.stk_min[-1])
        self.stk_min.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.stk_min.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk_min[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()