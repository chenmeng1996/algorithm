

from typing import List


"""
https://leetcode.cn/problems/max-dot-product-of-two-subsequences/

请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。
比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。

"""
def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
    """
    f[i][j] 表示只考虑数组nums1的前i个元素以及数组nums2的前j个元素时,
    可以得到的两个长度相同的非空子序列的最大点积。

    可以考虑每个数组中的最后一个元素:
    1. 选择成为点积。
    2. 不选择成为点积。
    """
    m, n = len(nums1), len(nums2)
    f = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            xij = nums1[i] * nums2[j]
            f[i][j] = xij
            if i > 0:
                f[i][j] = max(f[i][j], f[i - 1][j])
            if j > 0:
                f[i][j] = max(f[i][j], f[i][j - 1])
            if i > 0 and j > 0:
                f[i][j] = max(f[i][j], f[i - 1][j - 1] + xij)
    
    return f[m - 1][n - 1]