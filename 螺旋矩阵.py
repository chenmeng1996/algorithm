

from typing import List

"""
https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/

按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    上下左右四个边界条件, 每遍历一个方向就更新。
    """
    m = len(matrix)
    n = len(matrix[0])
    l, r, t, b = 0, n - 1, 0, m - 1
    res = []
    num = 0
    while num <= n * m:
        # 从左到右(上边界+1)
        for i in range(l, r + 1):
            res.append(matrix[t][i])
            num += 1
        t += 1
        # 从上到下(右边界-1)
        if num == n * m:
            break
        for i in range(t, b + 1):
            res.append(matrix[i][r])
            num += 1
        r -= 1
        # 从右到左(下边界-1)
        if num == n * m:
            break
        for i in range(r, l - 1, -1):
            res.append(matrix[b][i])
            num += 1
        b -= 1
        # 从下到上(左边界+1)
        if num == n * m:
            break
        for i in range(b, t - 1, -1):
            res.append(matrix[i][l])
            num += 1
        l += 1
    return res


if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = spiralOrder(matrix)
    print(res)