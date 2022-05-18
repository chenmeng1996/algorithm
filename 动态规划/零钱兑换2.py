

from typing import List

"""
https://leetcode.cn/problems/coin-change-2/

凑成总金额的硬币组合数。
"""
def change(amount: int, coins: List[int]) -> int:
    """
    动态规划。
    完全背包。

    dp[i]表示金额为i的组合数。
    dp[i] = sum(dp[i-j]) j是可用的硬币金额。

    为了避免计算重复的组合, 先遍历coin, 再遍历amount。
    """
    dp = [1] + [0]*amount
    for j in coins:
        for i in range(1, amount+1):
            if i - j >= 0:
                dp[i] += dp[i-j]
    return dp[amount]


if __name__ == "__main__":
    res = change(5, [1,2,5])
    print(res)