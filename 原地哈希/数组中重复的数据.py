

from typing import List

"""
https://leetcode.cn/problems/find-all-duplicates-in-an-array/
"""
def findDuplicates(nums: List[int]) -> List[int]:
    """
    原地哈希。
    需要将数i 放在数组中下标为 i-1 的位置。
    将元素与对应的下标位置的元素做交换。直到待交换的两个元素相等为止。
    """
    for i in range(len(nums)):
        # 一直对i位置的元素做交换，直到i元素与下标元素相同。
        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    res = []
    for i in range(len(nums)):
        # 元素与下标不一致，说明因为有重复元素，导致不能交换位置。
        if nums[i] - 1 != i:
            res.append(nums[i])
    return res