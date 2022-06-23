

from collections import defaultdict
import copy
from typing import List


"""
https://leetcode-cn.com/problems/eight-queens-lcci/
"""
def solveNQueens(n: int) -> List[List[str]]:
    """
    回溯。
    斜线为从左上到右下方向，同一条斜线上的每个位置满足行下标与列下标之差相等。
    斜线为从右上到左下方向，同一条斜线上的每个位置满足行下标与列下标之和相等。
    """
    def helper(row, visited_col, diagonal1, diagonal2, res, cur):
        if row >= n:
            res.append(copy.deepcopy(cur))
            return
        for i in range(n):
            if visited_col[i]:
                continue
            if row-i in diagonal1 or row+i in diagonal2:
                continue
            visited_col[i] = True
            diagonal1.add(row-i)
            diagonal2.add(row+i)
            cur.append(i)
            helper(row+1, visited_col, diagonal1, diagonal2, res, cur)
            visited_col[i] = False
            diagonal1.remove(row-i)
            diagonal2.remove(row+i)
            cur.pop()
    
    visited_col = [False]*n
    res = []
    cur = []
    diagonal1 = set()
    diagonal2 = set()
    helper(0, visited_col, diagonal1, diagonal2, res, cur)
    res1 = []
    for one_res in res:
        res2 = []
        for index in one_res:
            line = ["."]*n
            line[index] = "Q"
            s = "".join(line)
            res2.append(s)
        res1.append(res2)
    return res1


if __name__ == "__main__":
    res = solveNQueens(5)
    print(res)