
from typing import List

'''
输入为一个 n * n 的二维数组 matrix，请你计算从第一行落到最后一行，经过的路径和最小为多少。
每次下降，可以向下、向左下、向右下三个方向移动一格。
dp[i][j]表示matrix[i][j]为起点，到最后一行经过的路径和最小值。
dp[i][j] = min(dp[i+1][j]+matrix[i][j], dp[i+1][j-1]+matrix[i][j], dp[i+1][j+1]+matrix[i][j])
'''
def min_falling_path_sum(matrix: List[List[int]]):
    row_num = len(matrix)
    col_num = len(matrix[0])
    dp = [[None for _ in range(col_num)] for _ in range(row_num)]
    min_res = None
    # 第一行的不同位置作为起点
    for j in range(col_num):
        res = min_falling_path_sum_helper(matrix, 0, j, dp)
        if min_res is None or min_res > res:
            min_res = res
    return min_res

def min_falling_path_sum_helper(matrix: List[List[int]], i, j, dp):
    row_num = len(matrix)
    col_num = len(matrix[0])
    min_res = None
    # base case：最后一行
    if i == row_num - 1:
        return matrix[i][j]
    if i + 1 < row_num:
        if dp[i+1][j] is None:
            dp[i+1][j] = min_falling_path_sum_helper(matrix, i+1, j, dp)
        if min_res is None or min_res > dp[i+1][j] + matrix[i][j]:
            min_res = dp[i+1][j] + matrix[i][j]
        if j - 1 >= 0:
            if dp[i+1][j-1] is None:
                dp[i+1][j-1] = min_falling_path_sum_helper(matrix, i+1, j-1, dp)
            if min_res is None or min_res > dp[i+1][j-1] + matrix[i][j]:
                min_res = dp[i+1][j-1] + matrix[i][j]
        if j + 1 < col_num:
            if dp[i+1][j+1] is None:
                dp[i+1][j+1] = min_falling_path_sum_helper(matrix, i+1, j+1, dp)
            if min_res is None or min_res > dp[i+1][j+1] + matrix[i][j]:
                min_res = dp[i+1][j+1] + matrix[i][j]
    return min_res


if __name__ == "__main__":
    res = min_falling_path_sum([[2,1,3],[6,5,4],[7,8,9]])
    print(res)