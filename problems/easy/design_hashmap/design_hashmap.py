class MyHashMap:

    def __init__(self):
        self.hashmap = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        k = self.func_hash(key)
        for item in self.hashmap[k]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.hashmap[k].append([key, value])

    def get(self, key: int) -> int:
        k = self.func_hash(key)
        for item in self.hashmap[k]:
            if item[0] == key:
                return item[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        k = self.func_hash(key)
        to_del = None
        i = 0
        while i < len(self.hashmap[k]):
            if key == self.hashmap[k][i][0]:
                to_del = self.hashmap[k][i]
                break
            i += 1
        if to_del:
            self.hashmap[k].remove(to_del)

        # for item in self.hashmap[k]:
        #     if key == item[0]:
        #         to_del = item
        #         break
        # if to_del:
        #     self.hashmap[k].remove(to_del)

    def func_hash(self, val: int) -> int:
        return val % 1000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
