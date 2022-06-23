

from typing import List


"""
https://leetcode.cn/problems/unique-paths-ii/

有障碍物。
"""
def uniquePathsWithObstacles(grid: List[List[int]]) -> int:
    """
    动态规划。
    dp[i][j]表示左上角到[i,j]位置的不同路径数。
    如果grid[i][j] == 1(即有障碍), 则dp[i][j]=0
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            else:
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]


if __name__ == "__main__":
    grid = [
        [0, 1],
        [0, 0]
    ]
    res = uniquePathsWithObstacles(grid)
    print(res)