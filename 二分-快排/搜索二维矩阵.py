
import bisect
from typing import List


"""
https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
"""
def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    """
    从右上角看，类似一个二叉搜索树。
    从右上角开始，如果当前元素小于target，往左移动一格，如果当前元素小于target，往右移动一格。
    """
    if len(matrix) == 0:
        return False
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    i = 0
    j = col
    while i <= row and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
    return False





if __name__ == "__main__":
    # matrix = [
    #     [1,   4,  7, 11, 15],
    #     [2,   5,  8, 12, 19],
    #     [3,   6,  9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    res = findNumberIn2DArray(matrix, 20)
    print(res)