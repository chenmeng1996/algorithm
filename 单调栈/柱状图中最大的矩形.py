

from typing import List


"""
https://leetcode.cn/problems/largest-rectangle-in-histogram/
"""
def largestRectangleArea(heights: List[int]) -> int:
    """
    维护单调递增栈。
    单调栈存储下标。
    类似于【子数组的最小值之和】。

    当元素从栈删除时, 分别寻找左边比它大的和右边比它大的元素, 从而确定宽度。
    则以该元素为高度的矩形的最大面积 = 元素高度 * 宽度。
    """
    if len(heights) == 0:
        return 0
    stack = []
    n = len(heights)
    res = 0
    for i in range(n):
        while stack and heights[i] <= heights[stack[-1]]:
            x = stack.pop()
            # 确定左边界
            # 如果栈顶还有元素, 则栈顶元素+1是左边界
            # 如果栈顶没有元素, 则数组头是左边界
            if stack:
                left = stack[-1] + 1
            else:
                left = 0
            # 确定右边界, 右边界是i-1
            right = i - 1
            width = right - left + 1
            res = max(res, heights[x] * width)
        stack.append(i)
    
    # 遍历完成后，如果栈还有元素，弹出
    while stack:
        x = stack.pop()
        if stack:
            left = stack[-1] + 1
        else:
            left = 0
        right = n - 1
        width = right - left + 1
        res = max(res, heights[x] * width)
    
    return res


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    res = largestRectangleArea(heights)
    print(res)