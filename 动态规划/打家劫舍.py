
from typing import List

"""
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
"""
def rob(nums: List[int]) -> int:
    """
    dp[i]表示到i位置, 最大的偷盗金额.
    dp[n] = max{dp[i-2]+a[n], d[i-1]}
    dp[0] = a[0]
    dp[1] = max(dp[0], dp[1])
    """
    dp = [0] * len(nums)
    dp[0] = nums[0]
    if len(nums) > 1:
        dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    return dp[len(nums)-1]

def rob_my(nums: List[int]) -> int:
    """
    dp[i]表示最后偷的是i位置, 最大的偷盗金额.
    dp[n] = max{dp[i]} + a[n], 0 <= i <= n-2
    """
    dp = [0] * len(nums)
    for i in range(len(nums)):
        pre_max = 0
        for j in range(i-1):
            if dp[j] > pre_max:
                pre_max = dp[j]
        dp[i] = pre_max + nums[i]
    return max(dp)


if __name__ == "__main__":
    res = rob([2,7,9,3,1])
    print(res)