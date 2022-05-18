
from typing import List

"""
https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
"""
def findLengthOfShortestSubarray(nums: List[int]) -> int:
    """
    只能删除一个子数组, 则左边的子数组和右边的子数组是递增的, 且合并后也是递增的。
    所以从左往右寻找左边的子数组, 从右往左寻找右边的子数组。
    寻找到两个子数组后, 中间子数组必须删除。
    然后遍历左数组的元素作为左数组的尾部, 然后寻找右数组的头部使得数组连续。
    """
    n = len(nums)
    i = 0
    j = n-1

    # 寻找左边数组
    while i < n:
        if i < n-1 and nums[i] <= nums[i+1]:
            i += 1
        else:
            break

    # 数组已经有序
    if i == n-1:
        return 0
    
    # 寻找右边数组
    while j > i:
        if j > i+1 and nums[j] >= nums[j-1]:
            j -= 1
        else:
            break
    
    # 中间数组必须删除
    res = j - i - 1
    # 拼接左数组和右数组。寻找最大拼接长度。
    # 遍历左数组尾部，并寻找右数组的头部。
    # 这里不使用二分查找，而是使用双指针。
    max_len = 0
    y = j
    for x in range(0, i+1):
        while y < n:
            if nums[y] >= nums[x]:
                break
            else:
                y += 1
        max_len = max(max_len, x + 1 + n - y)
    
    # 考虑左数组全部删除 或 右数组全部删除
    max_len = max(max_len, i + 1, n - j)
    # 左数组和右数组的总长度
    total_len = i + 1 + n - j
    return res + total_len - max_len


if __name__ == "__main__":
    res = findLengthOfShortestSubarray([2,2,2,1,1,1])
    print(res)