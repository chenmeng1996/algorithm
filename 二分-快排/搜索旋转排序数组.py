
from typing import List

"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
def search(nums: List[int], target: int) -> int:
    """
    1. l <= mid > r, mid在更大的升序序列中。
        1. target < l或者target > mid, 在(mid, r)中递归寻找target。
        2. l < target < mid, 在(l, mid)中递归寻找target。
    2. l > mid <= r, mid在更小的升序序列中。
        1. mid < target  <= r, 在(mid, r)中递归寻找target。
        2. target < mid或者target >= r, 在(l, mid)中递归寻找target。
    3. l < mid < target, mid在完整的升序序列中。根据二分查找查即可。
    """
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid] and nums[mid] > nums[r]:
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        elif nums[l] > nums[mid] and nums[mid] <= nums[r]:
            if nums[mid] < target and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return -1