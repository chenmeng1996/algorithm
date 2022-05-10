 
from typing import List

"""
https://leetcode-cn.com/problems/minimum-path-sum/
"""
def minPathSum(grid: List[List[int]]) -> int:
    """
    dp[i][j] = min(d[i-1][j], dp[i][j-1]) + grid[i][j]
    """
    if len(grid) == 0:
        return 0
    row = len(grid)
    col = len(grid[0])
    dp = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            min_value = 0
            if i - 1 >= 0:
                min_value = dp[i-1][j]
            if j - 1 >= 0:
                if min_value == 0:
                    min_value = dp[i][j-1]
                else:
                    min_value = min(dp[i-1][j], dp[i][j-1])
            dp[i][j] = min_value + grid[i][j]
    return dp[row-1][col-1]