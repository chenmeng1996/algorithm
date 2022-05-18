

from typing import List

"""
https://leetcode.cn/problems/spiral-matrix-ii/

给你一个正整数n, 生成一个包含 1 到 n^2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix。
"""
def generateMatrix(n: int) -> List[List[int]]:
    l, r, t, b = 0, n - 1, 0, n - 1
    res = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    while num <= n * n:
        # 从左到右(上边界+1)
        for i in range(l, r + 1):
            res[t][i] = num
            num += 1
        t += 1
        # 从上到下(右边界-1)
        for i in range(t, b + 1):
            res[i][r] = num
            num += 1
        r -= 1
        # 从右到左(下边界-1)
        for i in range(r, l - 1, -1):
            res[b][i] = num
            num += 1
        b -= 1
        # 从下到上(左边界+1)
        for i in range(b, t - 1, -1): # bottom to top
            res[i][l] = num
            num += 1
        l += 1
    return res