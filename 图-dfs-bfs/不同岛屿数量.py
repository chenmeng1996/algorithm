
from copy import deepcopy
from typing import List

"""
https://www.lintcode.com/problem/860

两个岛屿被认为是相同的, 当且仅当一个岛屿可以通过平移变换(不可以旋转、翻转)和另一个岛屿重合。
"""
def num_distinct_islands(grid: List[List[int]]) -> int:
    """
    以通过BFS/DFS得到每一个岛屿, 然后把每一个岛屿的形状放到 set 里, 最后 set 的大小就是答案。

    set里存储dfs路径, 路径是岛屿每个节点相对于起始节点的下标偏移量。
    """
    def dfs(start_i, start_j, i, j):
        if visited[i][j]:
            return
        visited[i][j] = True
        path.append((i-start_i, j-start_j))
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_i = i + x
            next_j = j + y
            if next_i < 0 or next_i > n-1 or next_j < 0 or next_j > m-1:
                continue
            if visited[next_i][next_j] or grid[next_i][next_j] == 0:
                continue
            dfs(start_i, start_j, next_i, next_j)
    
    n = len(grid)
    m = len(grid[0])
    shape_set = set()
    path = []
    visited = [[False]*m for _ in range(n)]
    for start_i in range(n):
        for start_j in range(m):
            if grid[start_i][start_j] == 0:
                continue
            dfs(start_i, start_j, start_i, start_j)
            if len(path) != 0:
                shape_set.add(tuple(deepcopy(path)))
            path.clear()
    return len(shape_set)


if __name__ == "__main__":
    grid = [
        [1,1,0,1,1],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1]]
    res = num_distinct_islands(grid)
    print(res)