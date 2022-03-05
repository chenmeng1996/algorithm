from tkinter import N
from typing import List

'''
nums是无序数组，找出最长递增子序列的长度。子序列不一定是连续的。
dp[i]表示以数组下标i为结尾的最长递增子序列的长度。
dp[n] = max(dp[1]+1, dp[2]+1, ..., dp[a]+1), 1<a<n且nums[a]<nums[n]
'''
def length_of_LIS(nums: List[int]) -> int:
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        max_len = 1
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] + 1 > max_len:
                max_len = dp[j] + 1
        dp[i] = max_len
    return max(dp)


if __name__ == "__main__":
    res = length_of_LIS([10,9,2,5,3,7,101,18])
    print(res)