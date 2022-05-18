from typing import List


"""
https://leetcode-cn.com/problems/combination-sum-iv/

不同 整数组成的数组 nums, 和一个目标整数 target。
请你从 nums 中找出并返回总和为 target 的元素组合的个数。

顺序不同的序列被视作不同的组合。
"""
def combinationSum4(nums: List[int], target: int) -> int:
    """
    完全背包。
    组合区分排序。

    dp[i] += dp[i-num]

    官方关于状态转移方程的解释不够清楚。我来解释一下.。

    先举个例子, nums = [1, 2, 3], target = 35.

    假设用1,2,3拼凑出35的总组合个数为y。我们可以考虑三种情况:
    1. 有效组合的末尾数字为1,这类组合的个数为 x1。我们把所有该类组合的末尾1去掉, x1即为在1,2,3中凑出35 - 1 = 34的总组合个数。
    1. 有效组合的末尾数字为2,这类组合的个数为 x2。我们把所有该类组合的末尾2去掉, x1即为在1,2,3中凑出35 - 2 = 33的总组合个数。
    1. 有效组合的末尾数字为3,这类组合的个数为 x3。我们把所有该类组合的末尾3去掉, x1即为在1,2,3中凑出35 - 3 = 32的总组合个数。

    y = x1 + x2 + x3。而x1, x2, x3又可以用同样的办法从子问题得到。
    """
    dp = [1] + [0]*target
    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]
    return dp[target]
