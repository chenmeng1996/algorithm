

from typing import List


"""
https://leetcode.cn/problems/longest-consecutive-sequence/

需要O(n)时间复杂度。
"""
def longestConsecutive(nums: List[int]) -> int:
    """
    哈希表。
    我们的目的是从连续序列中的最小的数字开始寻找连续序列。
    1. 将数字用set去重
    2. 遍历set, 取出一个数字, 如果该数字减1在set中, 那么这个数字不是连续序列中的最小值, 所以不使用它作为起点来寻找序列。
        如果该数字减1不在set中, 则这个数字是连续序列的最小值, 开始寻找序列。通过每次增加1, 在set中寻找。
    """
    nums_set = set(nums)
    res = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            cur_len = 1
            while num + 1 in nums_set:
                cur_len += 1
                num += 1
            res = max(res, cur_len)
    return res
        