
from typing import List
from sortedcontainers import SortedList


"""
https://leetcode-cn.com/problems/132-pattern/
"""
def find132pattern(nums: List[int]) -> bool:
    """
    从右往左枚举1元素，使用单调栈（递减）记录可能的2元素，如果遇到大的元素，那么这个元素可以作为3元素，
    并且把栈中小于3元素的弹出，记录最大的元素，作为可能的2元素的最大值（2越大，1越好找）。
    如果在枚举1元素的过程中，发现有最大的2元素，且1元素比它小，则成功找到。
    """
    stack = []
    max_k = float("-inf")
    stack.append(nums[-1])
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < max_k:
            return True
        while stack:
            if nums[i] > stack[-1]:
                # 当前元素可以作为3元素，那记录下可以作为2元素的最大元素
                max_k = max(max_k, stack.pop())
            else:
                break
        stack.append(nums[i])
    return False


def find132pattern2(nums: List[int]) -> bool:
    """
    枚举3，判断左侧最小的元素是否小于3，判断右侧的元素是否有大于左侧最小元素且小于3的（找右边大于左侧最小元素的最小元素，判断是否小于3）。
    左侧最小元素通过枚举迭代更新。
    
    右侧元素通过一个有序字典维护(或者用有序数组维护)，以logn复杂度查询和删除。

    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """
    if len(nums) < 3:
        return False
    left_min = nums[0]
    right_all = SortedList(nums[2:])
    for j in range(1, len(nums)-1):
        if left_min < nums[j]:
            index = right_all.bisect_right(left_min)
            if index < len(right_all) and right_all[index] < nums[j]:
                return True
        left_min = min(left_min, nums[j])
        right_all.remove(nums[j])
    return False
        

def find132pattern(nums: List[int]) -> bool:
    """
    如果数据不是数组，而是源源不断的数据流。
    需要从左到右枚举2元素。TODO
    """
    pass