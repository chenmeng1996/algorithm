

from typing import List

"""
https://leetcode-cn.com/problems/first-missing-positive/
"""
def firstMissingPositive(nums: List[int]) -> int:
    """
    1. 遍历数组，将数x(1<=x<=n)放在下标为x-1的位置上，这个过程涉及到数组的元素交换。
    2. 等所有x(1<=x<=n)都放到了合适的位置后，遍历数组，如果数组元素 != 数组下标+1，则答案就是它。
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] and nums[i] <= n and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
            x = nums[i]-1
            nums[i], nums[x] = nums[x], nums[i]
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


if __name__ == "__main__":
    res = firstMissingPositive([3,4,-1,1])
    print(res)