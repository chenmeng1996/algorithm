
"""
https://leetcode.cn/problems/global-and-local-inversions/

从右往左遍历数组, 保存见到的最小的数
"""
def isIdealPermutation(nums):
    n = len(nums)
    min_value = n
    for i in range(n-1, -1, -1):
        min_value = min(min_value, nums[i])
        if i >= 2 and nums[i-2] > min_value:
            return False
    return True