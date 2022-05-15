
from typing import List

"""
https://leetcode.cn/problems/trapping-rain-water/
"""
def trap(height: List[int]) -> int:
    """
    动态规划。

    当存在连续的递减和递增序列, 则这个序列可以接雨水。雨水的高度是左右的最小值。

    所以计算每个位置的左边的最大高度, 右边的最大高度。通过动态规划可以求解:
    left_max[i] = max(left_max[i-1], height[i])
    right_max[i] = max(right_max[i+1], height[i])

    则每个位置的雨水为min(left_max[i], right_max[i]) - height[i]
    """
    n = len(height)
    left_max = [0]*n
    right_max = [0]*n
    for i in range(n):
        if i == 0:
            left_max[i] = height[i]
        else:
            left_max[i] = max(left_max[i-1], height[i])
    for i in range(n-1, -1, -1):
        if i == n-1:
            right_max[i] = height[i]
        else:
            right_max[i] = max(right_max[i+1], height[i])
    
    res = 0
    for i in range(n):
        res += min(left_max[i], right_max[i]) - height[i]
    return res


def trap1(height: List[int]) -> int:
    """
    单调递减栈。感觉不如动态规划容易理解。
    """
    stack = []
    res = 0
    for i in range(len(height)):
        right_height = height[i]
        while stack and height[stack[-1]] < right_height:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            rain_width = i - left - 1
            rain_height = min(height[left], height[i]) - height[top]
            res += rain_width * rain_height
        stack.append(i)
    return res


if __name__ == "__main__":
    res = trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(res)