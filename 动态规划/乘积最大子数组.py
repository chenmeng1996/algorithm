

from typing import List

"""
https://leetcode-cn.com/problems/maximum-product-subarray/
"""
def maxProduct(nums: List[int]) -> int:
    """
    dp1[i]为以i结尾的连续子数组最大乘积。
    dp2[i]为以i结尾的连续子数组最小乘积。
    dp1[i] = max(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
    dp2[i] = min(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
    """
    n = len(nums)
    dp1 = [0]*n
    dp2 = [0]*n
    for i in range(n):
        if i == 0:
            dp1[i] = dp2[i] = nums[i]
        else:
            dp1[i] = max(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
            dp2[i] = min(dp1[i-1]*nums[i], dp2[i-1]*nums[i], nums[i])
    return max(dp1)