

"""
https://leetcode.cn/problems/jian-sheng-zi-lcof/
"""
def cuttingRope(n: int) -> int:
    """
    dp[i]表示长度为i的绳子剪切后的最大乘积。
    因为剪切后最少两段，我们取走第一段，剩下来的段的乘积必定也是对应长度绳子剪切后的最大乘积。
    所以:
    dp[i] = max(dp[i-j] * j, i), 1<=j<=i-1
    """
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2,n+1):
        a = max([dp[i-j]*j for j in range(1,i)])
        if i != n:
            dp[i] = max(a, i)
        else:
            dp[i] = a
    print(dp)
    return dp[n]


if __name__ == "__main__":
    res = cuttingRope(4)
    print(res)