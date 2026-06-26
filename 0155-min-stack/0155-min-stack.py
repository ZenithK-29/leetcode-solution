class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
      
        if not self.stack:
            self.stack.append(value)
            self.minStack.append(value)
        else:
            currentMin = min(self.minStack[-1], value)
            self.stack.append(value)
            self.minStack.append(currentMin)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()