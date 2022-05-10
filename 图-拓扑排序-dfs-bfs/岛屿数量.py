from typing import List


def numIslands(grid: List[List[str]]) -> int:
    """
    遍历每一个点作为起点，使用dfs或bfs寻找所有连接的点，寻找完后数量加1。
    使用辅助数组记录访问过的点。
    """
    if len(grid) == 0:
        return 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]

    def dfs(i, j, visited):
        visited[i][j] = True
        for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
            if i + x < 0 or i + x > row-1 or j + y < 0 or j + y > col-1:
                continue
            if grid[i+x][j+y] == "0" or visited[i+x][j+y]:
                continue
            dfs(i+x, j+y, visited)

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0" or visited[i][j]:
                continue
            dfs(i, j, visited)
            res += 1
    return res


if __name__ == "__main__":
    res = numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    print(res)