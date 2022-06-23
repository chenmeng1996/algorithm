
from typing import List

"""
https://leetcode-cn.com/problems/merge-intervals/

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""
def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    按照左边端点对区间排。然后按部就班的合并就好了。
    """
    intervals.sort()
    res = []
    for interval in intervals:
        if len(res) == 0:
            res.append(interval)
        else:
            last = res[-1]
            if last[0] <= interval[0] <= last[1]:
                if interval[1] > last[1]:
                    last[1] = interval[1]
            else:
                res.append(interval)
    return res