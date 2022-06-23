

from typing import List

"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

可以买卖无限次, 但必须卖完再买。
"""
def maxProfit(prices: List[int]) -> int:
    """
    贪心
    """
    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            res += prices[i] - prices[i-1]
    return res