

from typing import List


"""
https://leetcode.cn/problems/4sum/
"""
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """
    数组排序, 枚举前两个数。后面两个数使用双指针寻找。
    """
    nums.sort()
    n = len(nums)
    if n < 4:
        return []
    res = []

    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            t = target - nums[i] - nums[j]
            x, y = j+1, n-1
            while x < y:
                if x > j+1 and nums[x] == nums[x-1]:
                    x += 1
                    continue
                if y < n-1 and nums[y] == nums[y+1]:
                    y -= 1
                    continue
                if nums[x] + nums[y] < t:
                    x += 1
                elif nums[x] + nums[y] > t:
                    y -= 1
                else:
                    res.append([nums[i], nums[j], nums[x], nums[y]])
                    x += 1
                    y -= 1
    return res