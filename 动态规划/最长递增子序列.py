import bisect
from typing import List

"""
https://leetcode.cn/problems/longest-increasing-subsequence/

如果要求最长递增子序列的其中一个路径，而不是长度呢？

答案：dp[i]同时记录前一个dp的下标。遍历结束后，使用下标回溯。
"""
def length_of_LIS(nums: List[int]) -> int:
    """
    dp[i]表示以数组下标i为结尾的最长递增子序列的长度。
    dp[n] = max(dp[1]+1, dp[2]+1, ..., dp[a]+1), 1<a<n且nums[a]<nums[n]

    时间复杂度O(n^2)
    """
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        max_len = 1
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] + 1 > max_len:
                max_len = dp[j] + 1
        dp[i] = max_len
    return max(dp)

def length_of_LIS2(nums: List[int]) -> int:
    """
    贪心 + 二分查找  时间复杂度O(nlogn)

    贪心思想：如果要使上升子序列尽可能长，则我们需要使序列上升的尽可能慢，因此希望在每次序列尾部增加的元素尽可能小。
    
    设置数组d, d[i]表示子序列长度为i时, 子序列末尾元素的最小值。
    从左往右遍历, 动态更新数组d。最终数组存储的是每个长度的上升子序列的最小值。数组d是递增的。
    具体做法如下：
    1. 如果新元素大于d[-1], 则加入到数组d, 这个意思是更新子序列长度加1后的末尾最小值。
    2. 如果新元素小于d[-1], 则寻找数组d中刚好大于新元素的值(二分查找, O(logn)), 并替换。这个意思是更新对应子序列长度的末尾最小值。

    时间复杂度: O(nlogn)
    """
    d = []
    for v in nums:
        if len(d) == 0 or v > d[-1]:
            d.append(v)
        else:
            index = bisect.bisect_left(d, v)
            d[index] = v
    return len(d)


if __name__ == "__main__":
    res = length_of_LIS2([10,9,2,5,3,7,101,18])
    print(res)