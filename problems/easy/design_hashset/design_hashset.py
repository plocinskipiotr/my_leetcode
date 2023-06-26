class MyHashSet:

    def __init__(self):
        self.hasharray = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            k = self.func_hash(key)
            self.hasharray[k].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            k = self.func_hash(key)
            self.hasharray[k].remove(key)

    def contains(self, key: int) -> bool:
        k = self.func_hash(key)
        return key in self.hasharray[k]

    def func_hash(self, val: int) -> int:
        return val % 1000

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
