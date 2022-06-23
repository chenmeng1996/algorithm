

from typing import List


"""
https://leetcode-cn.com/problems/sum-of-subarray-minimums/
"""
def sumSubarrayMins(arr: List[int]) -> int:
    """
    单调栈。TODO
    维护单调递增栈，栈里存储下标。目的是寻找一个元素是哪些子数组的最小值。

    每弹出一个元素，往前和往后寻找该元素为最小值的子数组。即寻找左边界和右边界。
    
    往前有两种情况：
    1. 前面有更小的元素（即栈还有元素）。则左边界就是该元素。
    2. 前面没有更小的元素（即栈没有元素）。则左边界是数组头部。

    往后有两种情况：
    1. 还在入栈过程中。则右边界是当前入栈元素。
    2. 入栈过程完成，在出栈过程中。则右边界是数组尾部。

    寻找到左右边界后，左边长度为x, 右边长度为y，则组合数=x + y + 1 + x*y
    """
    stack = []
    res = 0
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            if stack:
                left = stack[-1] + 1
            else:
                left = 0
            right = i-1
            res += arr[index] * ((index-left) + (right-index) + 1 + (index-left)*(right-index))
        stack.append(i)
    
    while stack:
        index = stack.pop()
        if stack:
            left = stack[-1] + 1
        else:
            left = 0
        right = len(arr) - 1
        res += arr[index] * ((index-left) + (right-index) + 1 + (index-left)*(right-index))
    
    return res % (10**9 + 7)


if __name__ == "__main__":
    res = sumSubarrayMins([11,81,94,43,3])
    # res = sumSubarrayMins([3,1,2,4])
    print(res)