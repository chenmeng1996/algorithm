
from typing import List

"""
https://leetcode.cn/problems/minimum-falling-path-sum/
"""
def min_falling_path_sum(matrix: List[List[int]]):
    """
    dp1[i]表示从第一行到该行的第i列的最小路径和。
    dp2[i]表示下一行的第i列的最小路径和。
    dp2[i] = nums[i] + min(dp1[i-1], dp1[i], dp[i+1])
    """
    n = len(matrix)
    dp1 = [0]*n
    dp2 = [0]*n
    for i in range(n):
        for j in range(n):
            min_value = float("inf")
            for x in [-1, 0, 1]:
                if j + x < 0 or j + x > n - 1:
                    continue
                min_value = min(min_value, dp1[j+x])
            dp2[j] = matrix[i][j] + min_value
        for i in range(n):
            dp1[i] = dp2[i]
    return min(dp2)
    


if __name__ == "__main__":
    res = min_falling_path_sum([[2,1,3],[6,5,4],[7,8,9]])
    print(res)