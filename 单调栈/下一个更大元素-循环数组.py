from typing import List


"""
https://leetcode-cn.com/problems/next-greater-element-ii/
"""
def nextGreaterElements(nums: List[int]) -> List[int]:
    """
    从左往右，单调栈存储的是下标，单调栈存储的下标元素递减。遍历2n次，利用取余进行循环。（相当于拼接了两段数组）
    """
    res = [-1] * len(nums) # 记录 下标元素的右边第一个最大元素
    stack = []
    for i in range(2*len(nums)):
        index = i % len(nums)
        while stack:
            if nums[stack[-1]] < nums[index]:
                res[stack.pop()] = nums[index]
            else:
                break
        stack.append(index)
    return res