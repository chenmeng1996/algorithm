

from typing import List


"""
https://leetcode.cn/problems/target-sum/

给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式
TODO 弄懂动态规划的优化，写一下回溯+备忘录
"""
def findTargetSumWays(nums: List[int], target: int) -> int:
    """
    动态规划。
    01背包。

    dp[i][j]表示前i位数组的和为j的数目。
    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
    """
    n = len(nums)
    sum_value = sum(nums)
    # 不可能的情况
    if target > sum_value or target < -sum_value:
        return 0

    dp = [[0]*(2*sum_value + 1) for _ in range(n)]

    # dp的起始条件, 只有一个元素的情况
    # 考虑到-0和+0的情况
    dp[0][-nums[0] + sum_value] += 1
    dp[0][nums[0] + sum_value] += 1

    for i in range(1, n):
        # 和的可能范围在[-sum_value, sum_value]
        for j in range(-sum_value, sum_value+1):
            # 对负和做偏移，从而可以存储到数组中
            if j - nums[i] + sum_value >= 0:
                dp[i][j + sum_value] += dp[i-1][j - nums[i] + sum_value]
            if j + nums[i] + sum_value <= 2*sum_value:
                dp[i][j + sum_value] += dp[i-1][j + nums[i] + sum_value]
    
    return dp[n-1][target + sum_value]


def findTargetSumWays(nums: List[int], target: int) -> int:
    """
    动态规划。优化。
    """
    pass

def findTargetSumWays(nums: List[int], target: int) -> int:
    """
    dfs回溯 + 备忘录
    """
    pass

if __name__ == "__main__":
    res = findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)
    print(res)