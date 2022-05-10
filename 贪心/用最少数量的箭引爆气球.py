
from typing import List


"""
最少需要多少个箭, 才能把所有气球射爆
"""
def find_min_arrow_shots(points: List[List[int]]) -> int:
    """
    题目等价于, 最多有多少个无重叠区间. 因为最少需要这些箭, 才能把这些无重叠区间的气球射爆.
    这道题里, 边界重叠也算重叠.
    """
    points.sort(key=lambda x: x[1])
    right = points[0][1]
    count = 1
    for i in range(1, len(points)):
        if points[i][0] > right:
            count += 1
            right = points[i][1]
    return count