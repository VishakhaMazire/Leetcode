class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin == None or val<currMin:
            currMin = val
        self.stack.append((val, currMin))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]