

from typing import List

"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

最多保留2个重复数字。
原地修改数组, 并返回去重后的数组长度。
"""
def removeDuplicates(nums: List[int]) -> int:
    """
    双指针。

    慢指针指向下一个不重复元素应该在的位置。
    快指针寻找下一个不重复元素。

    slow之前的元素都是已经处理好的元素, 每个元素最多出现2次。
    如果fast = slow-2, 那么因为有序, 则一定有fast = slow-1。
    这样fast当前的元素就有3个重复了, 不应该保留fast。
    所以当且仅当 nums[slow - 2] = nums[fast]时, 当前待检查元素nums[fast] 不应该被保留。
    """
    if len(nums) <= 2:
        return len(nums)
    slow = fast = 2
    while fast < len(nums):
        if nums[fast] != nums[slow-2]:
            # 重复项不超过2个, 保留fast元素
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow