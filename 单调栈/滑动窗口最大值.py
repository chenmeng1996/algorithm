

import collections
from typing import List

"""
https://leetcode.cn/problems/sliding-window-maximum/
"""
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    单调递减队列。
    维护一个单调递减队列, 队列存储下标。当队列左边的下标超出滑动窗口当前位置, 则删除。
    """
    n = len(nums)
    que = collections.deque()
    # 初始化递减队列, 写入k个数
    for i in range(k):
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        que.append(i)
    
    # 最初窗口的最大值
    res = [nums[que[0]]]
    for i in range(k, n):
        # 添加新的元素，因为是单调递减队列，所以会把小的元素删除
        while que and nums[i] >= nums[que[-1]]:
            que.pop()
        que.append(i)
        # 左边元素判断是否超出窗口，超出则删除
        while que[0] <= i - k:
            que.popleft()
        # 最左边是当前窗口的最大值，记录
        res.append(nums[que[0]])
    
    return res