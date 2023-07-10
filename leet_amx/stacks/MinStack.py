class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_stack:
            min_val = min(val,self.min_stack[-1])
        else:
            min_val = val
        self.min_stack.append(min_val)
        self.stack.append(val)

    def pop(self) -> None:
        res = self.stack.pop()
        self.min_stack.pop()
        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]