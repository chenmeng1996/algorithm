
"""
https://leetcode.cn/problems/unique-paths/
"""
def uniquePaths(m: int, n: int) -> int:
    """
    动态规划。
    dp[i][j]表示左上角到[i,j]位置的不同路径数。
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]