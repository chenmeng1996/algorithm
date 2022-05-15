
from typing import List

"""
https://leetcode.cn/problems/house-robber-ii/
"""
def rob(nums: List[int]) -> int:
    """
    围成一圈, 即首尾不能连续偷.
    那么可以分成两种情况：排除尾, 排除首
    这两种情况都计算一下, 取大值即可
    """
    def rob_helper(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[len(nums)-1]
    if len(nums) == 1:
        return nums[0]
    return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))


if __name__ == "__main__":
    res = rob([1,2,3,1])
    print(res)