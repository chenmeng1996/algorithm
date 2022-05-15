

"""
https://leetcode.cn/problems/chou-shu-lcof/
"""
def nthUglyNumber(n: int) -> int:
    """
    动态规划。TODO
    dp[i]表示第i个丑数。i>=1。
    每个丑数乘以一次2, 3, 5得到后面的三个丑数。
    我们需要按顺序生成丑数, 就要判断前面的丑数乘以较小值和后面的丑数乘以较大值, 哪个比较小。
    使用p2, p3, p5三个指针, 指向当前丑数的下标。2*dp[p2], 3*dp[p3], 5*dp[p5]是接下来的三个丑数。
    取最小值做为接下来的丑数, 并将对应pi指针向前移动一位, 代表之前的丑数已经用乘过i。
    """
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    p2 = p3 = p5 = 1
    for i in range(2, n+1):
        dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        if dp[i] == dp[p2]*2:
            p2 += 1
        if dp[i] == dp[p3]*3:
            p3 += 1
        if dp[i] == dp[p5]*5:
            p5 += 1
    return dp[n]