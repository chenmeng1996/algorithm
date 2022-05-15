

from typing import List


"""
https://leetcode.cn/problems/candy/
"""
def candy(grades: List[int]) -> int:
    """
    遍历数组两次。
    1. 从左往右遍历。右边如果比左边分数高, 则糖比左边多一个。
    2. 从右往左遍历。左边如果比右边分数高, 则糖比右边多一个。
    """
    n = len(grades)
    nums = [0] * n
    for i in range(n):
        if i > 0 and grades[i] > grades[i - 1]:
            nums[i] = nums[i - 1] + 1
        else:
            nums[i] = 1
    
    for i in range(n - 2, -1, -1):
        if i < n - 1 and grades[i] > grades[i + 1] and nums[i] <= nums[i+1]:
            nums[i] = nums[i + 1] + 1
    
    return sum(nums)