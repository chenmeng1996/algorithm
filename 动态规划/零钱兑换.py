from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [-1]*(amount+1)
    for i in range(amount+1):
        if i == 0:
            dp[i] = 0
        else:
            for coin in coins:
                if i - coin >= 0:
                    if dp[i-coin] == -1:
                        continue
                    if dp[i] == -1 or dp[i] > dp[i-coin] + 1:
                        dp[i] = dp[i-coin]+1
    return dp[amount]