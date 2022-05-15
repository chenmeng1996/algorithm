
from typing import List
from sortedcontainers import SortedList


"""
https://leetcode-cn.com/problems/132-pattern/
"""
def find132pattern(nums: List[int]) -> bool:
    """
    枚举其中的 22 个下标时间复杂度为 O(n^2)，会超出时间限制。
    因此我们可以考虑枚举其中的 1 个下标，并使用合适的数据结构维护另外的 2 个下标的可能值。

    从右往左遍历, 构建单调递减栈. 单调栈中的栈头作为j。
    当新元素比栈头大, 则弹出栈头, 将新的栈头作为j。单调栈中被弹出的元素, 记录最大值作为k(k越大, i越好找)。保证了j > k。
    当新元素比栈头小, 且新元素比k小, 则是一个132模式。否则加入栈。
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