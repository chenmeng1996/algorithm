
import heapq


class MedianFinder:
    """
    一个小顶堆，一个大顶堆，大小各为一半
    """

    class ReversedInt(int):
        def __lt__(self, __x: int) -> bool:
            return super().__gt__(__x)
        def __gt__(self, __x: int) -> bool:
            return super().__lt__(__x)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        if len(self.min_heap) > 0 and num < self.min_heap[0]:
            heapq.heappush(self.max_heap, MedianFinder.ReversedInt(num))
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.min_heap) - len(self.max_heap) > 1:
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, MedianFinder.ReversedInt(x))
        if len(self.max_heap) - len(self.min_heap) > 1:
            x = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, int(x))


    def findMedian(self) -> float:
        if len(self.min_heap) == 0:
            return None
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]
        else:
            return (self.min_heap[0]+self.max_heap[0]) / 2


if __name__ == "__main__":
# Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(-1)
    print(obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())