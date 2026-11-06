class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float("inf")

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.currMin = min(value, self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.currMin = float("inf")

        for el in self.stack:
            self.currMin = min(el, self.currMin)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()