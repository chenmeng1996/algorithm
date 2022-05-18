

from typing import List

"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

只能保留一个重复数字。
原地修改数组, 并返回去重后的数组长度。
"""
def removeDuplicates(nums: List[int]) -> int:
    """
    双指针。
    (凡是删除重复项都可用快慢指针)
    慢指针指向下一个不重复元素应该在的位置。
    快指针寻找下一个不重复元素。
    (当fast和前一个元素不相同时, 说明找到了下一个不重复元素)
    """
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    slow = fast = 1
    while fast < len(nums):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow