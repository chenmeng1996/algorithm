

from typing import List

"""
https://leetcode.cn/problems/max-consecutive-ones-iii/
"""
def longestOnes(nums: List[int], k: int) -> int:
    """
    滑动窗口, 维护k的值。
    当k>0时, 右边窗口可以加入0并让k减1。
    当右边窗口遇到0而k=0时, 移动左边窗口, 如果跳过的是0, 则k减少1, 并重新移动右边窗口。
    """
    n = len(nums)
    res = 0
    zeros = 0
    l = r = 0
    while r < n:
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(r - l + 1, res)
        r += 1
    return res


if __name__ == "__main__":
    res = longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
    print(res)