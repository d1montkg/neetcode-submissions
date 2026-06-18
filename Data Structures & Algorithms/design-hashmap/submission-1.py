class MyHashMap:

    def __init__(self):
        self.set = []
        self.index = []

    def put(self, key: int, value: int) -> None:
        if key not in self.index:
            self.set.append([key, value])
            self.index.append(key)
        else:
            for i in range(len(self.set)):
                if self.set[i][0] == key:
                    self.set[i][1] = value

    def get(self, key: int) -> int:
        if key in self.index:
            for i in range(len(self.set)):
                if self.set[i][0] == key:
                    return self.set[i][1]
        return -1

    def remove(self, key: int) -> None:
        if key in self.index:
            for i in range(len(self.set)):
                if self.set[i][0] == key:
                    self.index.remove(self.set[i][0])
                    self.set.remove(self.set[i])
                    break          


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)