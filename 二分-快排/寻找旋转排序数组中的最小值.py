

from typing import List

"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
数组元素不重复。
"""
def findMin(nums: List[int]) -> int:
    """
    二分查找。
    考虑mid在左边的升序中，还是右边的升序中。
    """
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[left] <= nums[mid] and nums[mid] > nums[right]:
            left = mid + 1
        elif nums[left] > nums[mid] and nums[mid] <= nums[right]:
            right = mid
        elif nums[left] <= nums[mid] and nums[mid] <= nums[right]:
            return nums[left]
    return nums[left]


if __name__ == "__main__":
    res = findMin([3,1,2])
    print(res)