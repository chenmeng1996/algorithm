
import functools
import heapq
from typing import List


"""
https://blog.csdn.net/qq_20817327/article/details/107739258

给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[ s1 , e1 ] ，[ s2 , e2 ]，…] (si < ei) ，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

这道题目等价于： 最大重叠区间。
"""
def minMeetingRoom(intervals: List[List[int]]):
    """
    小顶堆。

    按照开始时间的顺序（开始时间相同，则按照结束时间的顺序），将会议入堆。结束时间最小的会议在堆顶。
    每次新会议入堆时，判断堆顶会议是否结束，如果结束则出堆。重复该步骤，直到堆顶会议和新会议同时在进行（重叠），
    那么此时新会议和堆中的所有会议都重叠。

    只需要记录堆的最大长度，即可知道最多同时有多少会议同时在进行。
    """
    def compare(x, y):
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        elif x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        return 0
    intervals.sort(functools.cmp_to_key(compare))
    heap = []
    max_len = 0
    for interval in intervals:
        while heap and interval[0] < heap[-1]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        max_len = max(max_len, len(heap))
    return max_len