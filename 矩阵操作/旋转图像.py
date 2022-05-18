from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    矩阵向右旋转90度，元素所在的行和列发生了反转。
    即 a[j,n-1-i] = a[i,j]
    但是a[j,n-1-i]会被覆盖，需要先把它旋转，以此往下推，需要先覆盖若干次。

    那么应该如何选择需要旋转的元素呢？把元素划分成四块对称的区域（区分矩阵长度是奇数或偶数的情况），取左上角区域即可。
    """
    n = len(matrix)
    for i in range(n//2):
        for j in range((n+1)//2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = tmp

