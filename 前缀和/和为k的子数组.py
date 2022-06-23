
from collections import defaultdict
from typing import List


"""
https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""
def subarraySum(nums: List[int], k: int) -> int:
    """
    定义pre[i]为以i结尾的子数组的和。
    那么求和为k的子数组个数。即求nums[i:j]=k的个数。即pre[j] - pre[i] = k。
    
    然后从前往后遍历。每遍历到一个节点j。根据pre[j] - pre[i] = k的公式。寻找pre[i]。
    那么如何快速寻找pre[i]呢。通过dict记录pre和的值出现了多少次。
    """
    cache = defaultdict(int)
    cache[0] = 1 # 和为0，初始化1次，比较重要
    pre = 0
    count = 0
    for j in range(len(nums)):
        pre += nums[j]
        target = pre - k
        if target in cache:
            # 从头开始且和为target的子数组数量
            count += cache[target]
        # 从头开始的子数组，且和为pre，数量又多了一个
        cache[pre] += 1
    return count

        