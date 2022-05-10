

"""
https://leetcode.cn/problems/design-hashmap/
"""

class MyHashMap:
    """
    数组 + 链表(python3没有链表，使用list代替)。
    """

    def __init__(self):
        self.length = 1000
        self.arr = [[] for _ in range(self.length)]


    def put(self, key: int, value: int) -> None:
        link = self.arr[self.hash(key)]
        for i in range(len(link)):
            if link[i][0] == key:
                link[i][1] = value
                return None
        link.append([key, value])
        

    def get(self, key: int) -> int:
        link = self.arr[self.hash(key)]
        for i in range(len(link)):
            if link[i][0] == key:
                return link[i][1]
        return -1


    def remove(self, key: int) -> None:
        link = self.arr[self.hash(key)]
        index = -1
        for i in range(len(link)):
            if link[i][0] == key:
                index = i
                break
        if index == -1:
            return
        link[index], link[-1] = link[-1], link[index]
        link.pop()


    def hash(self, key: int):
        return key % self.length