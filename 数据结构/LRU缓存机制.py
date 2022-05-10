class LRUCache:
    """
    哈希表 + 双向链表，实现LRU缓存队列
    """
    class DLinkedNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.size = 0
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.move_to_tail(self.cache[key])
            self.cache[key].value = value
        else:
            if self.size >= self.capacity:
                node = self.delete_first_node()
                del self.cache[node.key]
                self.size -= 1
            new_node = self.DLinkedNode(key, value)
            self.add_to_tail(new_node)
            self.cache[key] = new_node
            self.size += 1

    def move_to_tail(self, node: DLinkedNode) -> None:
        # node节点从链表删除
        node.prev.next = node.next
        node.next.prev = node.prev
        # node节点插入到tail节点前
        self.add_to_tail(node)

    def add_to_tail(self, node: DLinkedNode) -> None:
        # node节点插入到tail节点前
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def delete_first_node(self) -> DLinkedNode:
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node


import collections
class LRUCacheEasy(collections.OrderedDict):
    """
    OrderedDict实现了哈希表+双链表
    """
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
