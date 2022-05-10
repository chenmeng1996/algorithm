

from typing import List

"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
数组中数字可能重复。
"""
def minArray(numbers: List[int]) -> int:
    """
    二分查找
    """
    l = 0
    r = len(numbers) - 1
    while l <= r:
        if l == r:
            return numbers[l]
        mid = (l+r) // 2
        if numbers[mid] < numbers[r]:
            r = mid
        elif numbers[mid] > numbers[r]:
            l = mid + 1
        else:
            r -= 1
    return numbers[mid]


if __name__ == "__main__":
    res = minArray([2,2,2,0,1])
    print(res)