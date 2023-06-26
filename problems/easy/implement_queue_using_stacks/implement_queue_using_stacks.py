class MyQueue:

    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def AtoB(self, aStack, bStack):
        while aStack:
            bStack.append(aStack.pop())

    def push(self, x: int) -> None:
        self.AtoB(self.s1, self.s2)
        self.s1.append(x)
        self.AtoB(self.s2, self.s1)

    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        if not self.s2:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
