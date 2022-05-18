

from collections import deque
from typing import List

"""
https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

给你一个整数数组 nums, 和一个表示限制的整数 limit。
请你返回最长连续子数组的长度，
该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
"""
def longestSubarray(nums: List[int], limit: int) -> int:
    """
    滑动窗口 + 单调队列.
    仅需要统计当前窗口内的最大值与最小值，可以分别使用两个单调队列。
    一个单调递增的队列min_que维护最小值,
    一个单调递减的队列max_que维护最大值。
    这样我们只需要计算两个队列的队首的差值, 即可知道当前窗口是否满足条件。
    """
    n = len(nums)
    max_que = deque()
    min_que = deque()
    left = right = res = 0

    while right < n:
        while max_que and max_que[-1] < nums[right]:
            max_que.pop()
        while min_que and min_que[-1] > nums[right]:
            min_que.pop()
        
        max_que.append(nums[right])
        min_que.append(nums[right])

        while max_que and min_que and max_que[0] - min_que[0] > limit:
            if nums[left] == min_que[0]:
                min_que.popleft()
            if nums[left] == max_que[0]:
                max_que.popleft()
            left += 1
        
        res = max(res, right - left + 1)
        right += 1
    
    return res