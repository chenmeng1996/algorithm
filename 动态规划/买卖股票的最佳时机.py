

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    """
    遍历，每次记录价格的最小值、历史利益的最大值（当前价格-价格最小值，并与历史利益最大值比较）
    """
    minprice = float("inf")
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit


def maxProfit(prices: List[int]) -> int:
    """
    动态规划。
    用相邻天数的股票差值生成一个新的数组。
    求最大利益，即求新数组的连续子数组最大和。
    """
    if len(prices) in [0, 1]:
        return 0
    diff = []
    for i in range(1, len(prices)):
        diff.append(prices[i]-prices[i-1])
    dp = [0] * len(diff)
    dp[0] = diff[0]
    for i in range(1, len(diff)):
        if dp[i-1] < 0:
            dp[i] = diff[i]
        else:
            dp[i] = dp[i-1] + diff[i]
    return max(max(dp), 0)
