"""
https://leetcode-cn.com/problems/hanota-lcci/
"""

from typing import List


def hanota(A: List[int], B: List[int], C: List[int]) -> None:
    """
    Do not return anything, modify C in-place instead.
    """
    def move(A, B, C, n):
        if n == 1:
            C.append(A.pop())
            return
        move(A, C, B, n-1)
        move(A, B, C, 1)
        move(B, A, C, n-1)
    move(A, B, C, len(A))


if __name__ == "__main__":
    A = [1, 2, 3]
    B = []
    C = []
    hanota(A, B, C)
    print(C)