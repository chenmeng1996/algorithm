

from typing import List

"""
https://leetcode-cn.com/problems/next-greater-element-i/
"""
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    单调栈。

    一但要求下一个更大的元素，就是用单调栈解，力扣题库相似的题目都是这个解法。
    
    想办法先求出nums2中每个元素右边的第一个比它大的元素。
    方法是从左往右，构建单调递减的单调栈。并用哈希表存储每个元素右边第一个比它大的元素。
    """
    res = {}
    stack = []
    for v in nums2:
        while stack and v > stack[-1]:
            x = stack.pop()
            res[x] = v
        stack.append(v)
    while stack:
        res[stack.pop()] = -1
    return [res[v] for v in nums1]