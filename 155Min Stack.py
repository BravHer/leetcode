class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]
        self.length = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.length == 0:
            self.minstack.append(x)
        elif x < self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])
        self.length += 1

    def pop(self) -> None:
        if self.length == 0:
            return False
        self.stack.pop()
        self.minstack.pop()
        self.length -=1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]