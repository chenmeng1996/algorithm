

import heapq
from typing import List

"""
https://leetcode.cn/problems/trapping-rain-water-ii/

柱子是一二维数组。
"""
def trapRainWater(heightMap: List[List[int]]) -> int:
    """
    [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    能够接雨水的位置满足以下条件:
    1. 不在最外围。
    2. 自身高度比上下左右四个相邻方块接水后的高度都低。

    从最外围开始, 使用最小堆维护外围的最小高度和位置。从最小高度的位置开始, 计算相邻内围是否可以乘雨水。
    """
    if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    # 柱子是否被访问
    visited = [[0]*n for _ in range(m)]
    heap = []
    for i in range(m):
        for j in range(n):
            # 最外层柱子
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                visited[i][j] = 1
                heapq.heappush(heap, (heightMap[i][j], i, j))
    
    res = 0
    while heap:
        # 当前外围的最小高度的位置以及高度
        height, i, j = heapq.heappop(heap)
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            # 遍历当前位置的上下左右4个位置, 寻找内围没有被访问的位置
            next_i, next_j = i + x, j + y
            if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n and visited[next_i][next_j] == 0:
                # 内围位置的高度比外围的最小高度低，则可以接雨水
                if height > heightMap[next_i][next_j]:
                    res += height - heightMap[next_i][next_j]
                visited[next_i][next_j] = 1    
                # 内围成为新的外围。如果内围高度比外围低, 则盛满雨水后高度相同；如果内围高度比外围高, 则使用内围高度
                heapq.heappush(heap, (max(height, heightMap[next_i][next_j]), next_i, next_j))
    return res