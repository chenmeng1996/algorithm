

from typing import List

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
def maxProfit(prices: List[int]) -> int:
    """
    dp[i][j][k]表示第i天，买了j次，卖了k次，此时的利润。其中0<=j,k<=2

    dp[i][0][0] = 0
    dp[i][1][0] = max(dp[i-1][1][0], -prices[i])
    dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0]+prices[i])
    dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][1]-prices[i])
    dp[i][2][2] = max(dp[i-1][2][2], dp[i-1][2][1]+prices[i])

    从上可知，dp[i]只与dp[i-1]有关，所以设：
    dp[i][1][0] = buy1
    dp[i][1][1] = sell1
    dp[i][2][1] = buy2
    dp[i][2][2] = sell2

    buy1 = max(buy1, -price[i])
    sell1 = max(sell1, buy1 + prices[i])
    buy2 = max(buy2, sell1-prices[i])
    sell2 = max(sell2, buy2+prices[i])
    """
    buy1 = sell1 = buy2 = sell2 = float("-inf")
    for v in prices:
        buy1_tmp = max(buy1, -v)
        sell1_tmp = max(sell1, buy1 + v)
        buy2_tmp = max(buy2, sell1 - v)
        sell2_tmp = max(sell2, buy2 + v)
        buy1 = buy1_tmp
        sell1 = sell1_tmp
        buy2 = buy2_tmp
        sell2 = sell2_tmp
    return max(sell1, sell2, 0)