

from functools import cmp_to_key
from operator import le
from typing import List, Tuple


"""
假设有一系列的从起点到终点的路径，形如[(start1, end1), (start2, end2), (start3, end3), ...].
现在需要保证同一个节点上最多只有3条经过的路径, 问最少删掉多少路径就可以满足要求.
"""
def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    选三次最多无重叠区间,结果就是每个节点最多有3条经过路径的最大区间数
    """
    total = 0
    length = len(intervals)
    for _ in range(3):
        intervals, count = max_unoverlap_intervals(intervals)
        total += count
    return length - total


# 最大不重叠的区间数，并且删除已经选中的区间
def max_unoverlap_intervals(intervals: List[List[int]]) -> Tuple[list, int]:
    """
    这道题等价于, 这个区间集合最多有多少个不重合区间(边界也算重合).
    按照end对区间排序, 并从end最小的区间开始, 按照贪心策略, 选择区间, 并去除与该区间重叠的区间, 并继续按照该策略进行.
    """
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    right = intervals[0][1]
    new_intervals = []
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] > right:
            count += 1
            right = intervals[i][1]
        else:
            new_intervals.append(intervals[i])
    return new_intervals, count


if __name__ == "__main__":
    res = erase_overlap_intervals([[1,3], [2,4], [3,4], [3,5], [4,5], [4,6], [5,6] ])
    print(res)