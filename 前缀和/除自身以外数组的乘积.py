


from typing import List

"""
https://leetcode.cn/problems/product-of-array-except-self/
"""
def productExceptSelf(nums: List[int]) -> List[int]:
    """
    计算 前缀乘积 和 后缀乘积。
    """
    length = len(nums)
    left, right, res = [0]*length, [0]*length, [0]*length
    
    # 左侧第一个元素的左乘积为1
    left[0] = 1
    for i in range(1, length):
        left[i] = nums[i - 1] * left[i - 1]
    
    # 右侧第一个元素的右乘积为1
    right[length - 1] = 1
    for i in range(length-2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]

    for i in range(length):
        res[i] = left[i] * right[i]
    
    return res