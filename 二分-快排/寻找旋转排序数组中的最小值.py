

from typing import List

"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""
def findMin(nums: List[int]) -> int:
    """
    二分查找。
    考虑mid在左边的升序中, 还是右边的升序中。最小值在右边的升序中。
    """
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) // 2
        # 在左边的升序中
        if nums[mid] > nums[right]:
            left = mid + 1
        # 在右边的升序中
        else:
            right = mid
    return nums[left]


if __name__ == "__main__":
    res = findMin([3,1,2])
    print(res)