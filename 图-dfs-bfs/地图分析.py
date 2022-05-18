

from collections import deque
from typing import List

"""
https://leetcode.cn/problems/as-far-from-land-as-possible/
"""
def maxDistance(grid: List[List[int]]) -> int:
    """
    bfs。
    选择每个海洋作为起点, 通过bfs计算离它最近的陆地距离。

    时间复杂度: 单次bfs是O(n^2), 最多执行n^2次bfs, 所以是O(n^4)
    空间复杂度: O(n^2)
    """
    def bfs(start_i, start_j):
        que = deque()
        visited = [[False]*n for _ in range(n)]
        que.append((start_i, start_j))
        visited[start_i][start_j] = True
        while que:
            i, j = que.popleft()
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_i, next_j = i + x, j + y
                if next_i < 0 or next_i > n -1 or next_j < 0 or next_j > n - 1:
                    continue
                if visited[next_i][next_j]:
                    continue
                visited[i][j] = True
                if grid[next_i][next_j] == 0:
                    que.append((next_i, next_j))
                else:
                    return abs(next_i-start_i) + abs(next_j-start_j)
        # 没有陆地
        return -1

    n = len(grid)
    min_distance = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                if min_distance is None:
                    min_distance = bfs(i, j)
                else:
                    min_distance = max(min_distance, bfs(i, j))
    # 没有海洋
    if min_distance is None:
        return -1
    else:
        return min_distance
    

def maxDistance(grid: List[List[int]]) -> int:
    """
    多源bfs。

    找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。
    等价于: 从所有陆地开始bfs, 最后遍历到的海洋。

    选择所有陆地作为大的起点, 通过bfs计算离大起点最近的海洋距离。

    时间复杂度: 遍历每个节点一次, 所以是O(n^2)
    空间复杂度: O(n^2)
    """
    # BFS 宽度优先搜索 向外一层层扩散
    n = len(grid)
    land = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                land.append([x, y])

    if len(land) == 0 or len(land) == n*n:
        return -1

    res = -1

    while land:
        res += 1
        # 储存即将检索的海洋坐标, 作为下一轮bfs的起点
        new_land = [] 
        for land_i, land_j in land:
            for x, y in [(0,-1), (1,0), (0,1), (-1,0)]:
                next_i, next_j = land_i + x, land_j + y
                if next_i < 0 or next_i > n-1 or next_j < 0 or next_j > n-1:
                    continue
                # 遇见海洋, 将海洋设置为已访问
                if grid[next_i][next_j] == 0:
                    grid[next_i][next_j] = 2
                    new_land.append((next_i, next_j))
        land = new_land

    return res