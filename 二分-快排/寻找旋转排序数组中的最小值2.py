

from typing import List

"""
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/
"""
def findMin(nums: List[int]) -> int:
    """
    二分查找
    考虑mid在最小值的左侧还是右侧。
    1. nums[mid] < nums[right], 则mid在最小值的右侧, 可以忽略右半段。
    2. nums[mid] > nums[right], 则mid在最小值的左侧, 可以忽略左半段。
    3. nums[mid] == nums[right], 因为有重复元素, 不能确定mid的位置, 但可以确定right删除也没有关系(因为有重复元素mid), 所以right -= 1。
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        if l == r:
            return nums[l]
        mid = (l+r) // 2
        if nums[mid] < nums[r]:
            r = mid
        elif nums[mid] > nums[r]:
            l = mid + 1
        else:
            r -= 1
    return nums[mid]


if __name__ == "__main__":
    res = findMin([2,2,2,0,1])
    print(res)