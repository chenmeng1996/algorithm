
from typing import List

def dicesProbability(n: int) -> List[float]:
    """
    二维动态规划。
    
    n个骰子，一共有6**n种投递方式。只需要知道数字x有多少种投递方式即可。
    
    假设已知n-1个骰子，数字x-1, x-2, x-3, x-4, x-5, x-6的投递方式次数。
    因为第n个骰子的数字是1~6，所以n个骰子，数字x的投递次数为上述投递次数相加。

    设dp[i][j]为i个骰子投出数字总和为j的次数。
    dp[i][j]=sum(dp[i-1][j-n]), 1<=n<=6

    dp[1][n]=1, 1<=n<=6
    """
    dp = [[0]*(n*6+1) for _ in range(n+1)]
    for i in range(1,7):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(i, i*6+1):
            dp[i][j] = sum([dp[i-1][j-v] for v in range(1, 7)])
    total = 6**n
    return [dp[n][j] / total for j in range(n, n*6+1)]


if __name__ == "__main__":
    res = dicesProbability(2)
    print(res)
