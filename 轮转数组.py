from typing import List

"""
https://leetcode-cn.com/problems/rotate-array/
空间复杂度要O(1)
"""
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.

    先整体反转数组，再将两段数组再反转一次
    """
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    n = len(nums)
    k = k % n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    