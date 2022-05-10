

from typing import List

"""
https://leetcode-cn.com/problems/next-greater-element-i/
"""
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    单调栈。

    一但要求下一个更大的元素，就是用单调栈解，力扣题库相似的题目都是这个解法。
    
    想办法先求出nums2中每个元素右边的第一个比它大的元素。
    方法是从右往左，构建单调递减的单调栈。并用哈希表存储每个元素右边第一个比它大的元素。
    """
    res = {}
    stack = []
    for v in nums2[-1::-1]:
        # 先把栈中小于当前元素的删除
        while stack:
            if stack[-1] < v:
                stack.pop()
            else:
                break
        # 剩下的栈顶元素是当前元素右边的第一个比它大元素，如果栈为空，说明没有右边没有比它大的元素
        if stack:
            res[v] = stack[-1]
        else:
            res[v] = -1
        # 当前元素入栈
        stack.append(v)
    return [res[v] for v in nums1]