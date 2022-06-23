
from typing import List


"""
https://www.lintcode.com/problem/850/description
"""
def employee_free_time(schedule: List[List[int]]) -> List[List[int]]:
    """
    合并区间
    """
    # Write your code here
    intervals = []
    for sche in schedule:
        i = 0
        while i < len(sche):
            intervals.append([sche[i], sche[i+1]-1])
            i += 2
    intervals.sort()
    res = []
    record = []
    for interval in intervals:
        if len(record) == 0 or interval[0] > record[-1][1]:
            intervals.append(interval)
        else:
            record[-1][1] = interval[1]
    for i in len(record):
        if i < len(record)-1:
            if record[i][1] != record[i+1][0]:
                res.append([record[i][1], record[i+1][0]+1])
    return res