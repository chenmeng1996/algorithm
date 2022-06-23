from collections import deque


class LRUCache:
    """
    哈希表加双向链表。
    哈希表维护key-value。
    双向链表维护key的顺序。

    python有OrderedDict
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.link = deque()


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.link.remove(key)
        self.link.appendleft(key)
        return self.dict[key]


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.link.remove(key)
        else:
            if len(self.link) == self.capacity:
                k = self.link.pop()
                self.dict.pop(k)
        self.link.appendleft(key)
        self.dict[key] = value
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)