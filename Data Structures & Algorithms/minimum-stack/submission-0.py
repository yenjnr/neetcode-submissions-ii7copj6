class MinStack:

    def __init__(self):
        self.stack = []
        self.least = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.least = val
        else:
            self.stack.append(val - self.least)
            if val < self.least:
                self.least = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        if pop < 0:
            self.least = self.least - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.least
        else:
            return self.least

    def getMin(self) -> int:
        return self.least
