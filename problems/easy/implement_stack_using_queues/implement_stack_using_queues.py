class MyStack:

    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1 - 1):
            self.queue.append(self.queue.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if not len(self.queue):
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
