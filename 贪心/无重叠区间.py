

from functools import cmp_to_key
from operator import le
from typing import List


"""
给定一个区间的集合 intervals, 其中 intervals[i] = [starti, endi], 返回 需要移除区间的最小数量, 使剩余区间互不重叠
"""
def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    这道题等价于, 这个区间集合最多有多少个不重合区间。
    按照end对区间排序, 并从end最小的区间开始, 按照贪心策略, 选择区间, 并去除与该区间重叠的区间, 并继续按照该策略进行.
    这种做法类似于一天有很多个会议，如何选择参加最多的会议。
    """
    intervals.sort(key=lambda x: x[1])
    right = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= right:
            count += 1
            right = intervals[i][1]
    return len(intervals) - count


if __name__ == "__main__":
    res = erase_overlap_intervals([ [1,2], [1,2], [1,2] ])
    print(res)