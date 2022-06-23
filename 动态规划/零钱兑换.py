from typing import List

"""
https://leetcode.cn/problems/coin-change/

凑成总金额所需的 最少的硬币个数。
"""
def coinChange(coins: List[int], amount: int) -> int:
    """
    完全背包

    dp[i]表示凑出总金额为i的最少硬币个数。

    dp[i] = min(dp[i], dp[i-num]+1)
    或者
    dp[i] = max(dp[i], dp[i-num]+1)
    """
    dp = [-1]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin < 0:
                continue
            if dp[i-coin] == -1:
                continue
            if dp[i] == -1:
                dp[i] = dp[i-coin]+1
            else:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount]