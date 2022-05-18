

from typing import List


"""
https://leetcode.cn/problems/unique-paths-iii/

在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
"""
def uniquePathsIII(grid: List[List[int]]) -> int:
    """
    dfs
    """
    def dfs(i, j):
        visited[i][j] = True
        path.append((i, j))
        if grid[i][j] == 2 and len(path) == total:
            count[0] += 1
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_i = i + x
            next_j = j + y
            if next_i < 0 or next_i > m-1 or next_j < 0 or next_j > n-1:
                continue
            if grid[next_i][next_j] == -1 or visited[next_i][next_j]:
                continue
            dfs(next_i, next_j)
        path.pop()
        visited[i][j] = False
    
    # 计算无障碍方格和起点、终点数量
    m = len(grid)
    n = len(grid[0])
    start = None
    total = 2
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                total += 1
            if grid[i][j] == 1:
                start = [i, j]
    
    visited = [[False]*n for _ in range(m)]
    path = []
    count = [0]
    dfs(start[0], start[1])
    return count[0]


if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    res = uniquePathsIII(grid)
    print(res)