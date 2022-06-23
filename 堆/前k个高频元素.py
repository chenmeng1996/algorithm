

from collections import defaultdict
import heapq
from typing import List


def topK_frequent(nums: List[int], k: int) -> List[int]:
    """
    先统计每个数出现的次数, 并按照次数构建小顶堆(小顶堆大小为k), 构建完成后, 堆里的k个元素就是前k个高频元素
    """
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    
    heap = []
    for num, count in counter.items():
        if len(heap) >= k:
            if count < heap[0][0]:
                continue
            else:
                heapq.heappop(heap)
        heapq.heappush(heap, (count, num))
    
    res = []
    for v in heap:
        res.append(v[1])
    return res
    

if __name__ == "__main__":
    res = topK_frequent([1,1,1,2,2,3], k = 2)
    print(res)