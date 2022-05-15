from typing import List


"""
https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""
def maxSubArray(nums: List[int]) -> int:
    """
    动态规划。
    dp[i]表示以i为终点的最大和。
    则dp[n] = max(dp[n-1]+nums[n], nums[n])
    """
    if len(nums) == 0:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)

    
def maxSubArray(nums: List[int]) -> int:
    """
    贪心。
    从左往右遍历，维护一个当前和cur_sum、最大和max_sum。如果累加当前值后，发现cur_sum<0，则应该甩掉前面的负担，从当前值开始。
    如果当前值大于0，则cur_sum=当前值，如果当前值小于0，则cur_sum=0。
    """
    max_sum = None
    current_sum = 0
    for v in nums:
        current_sum += v
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            if v > 0:
                current_sum = v
            else:
                current_sum = 0
    return max_sum


