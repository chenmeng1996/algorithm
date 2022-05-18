

"""
https://leetcode.cn/problems/distinct-subsequences/

给定一个字符串s和一个字符串t, 计算在s的子序列中t出现的个数。
"""
def numDistinct(s: str, t: str) -> int:
    """
    dp[i][j]表示在s[i:]的子序列中t[j:]出现的个数。

    1. dp[i][j] = dp[i+1][j+1] + dp[i+1][j], if s[i]==s[j]
    2. dp[i][j] = dp[i+1][j], if s[i]!=s[j]
    """
    m, n = len(s), len(t)
    if m < n:
        return 0
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][n] = 1
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]
    
    return dp[0][0]