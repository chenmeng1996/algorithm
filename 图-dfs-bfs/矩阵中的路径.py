
from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
def exist(board: List[List[str]], word: str) -> bool:
    """
    深度优先搜索
    """
    row = len(board)
    col = len(board[0])
    res = []
    visited = [[False] * col for _ in range(row)]

    def dfs(v, u, index):
        if len(res) != 0:
            return
        # 以(start,end) 为起点进行深度优先搜索
        if not (v >= 0 and v <= row and u >= 0 and u <=col):
            return
        if board[v][u] != word[index]:
            return
        visited[v][u] = True
        if index == len(word) - 1:
            res.append(True)
            return
        # 下一步，四种可能
        for x, y in [(0,-1), (0,1), (1,0), (-1,0)]:
            if v + x < 0 or v + x > row - 1 or u + y < 0 or u + y > col - 1:
                continue
            if visited[v+x][u+y]:
                continue
            dfs(v+x, u+y, index+1)
        # 四种可能走完，重新进入上一步
        visited[v][u] = False
        return

    for i in range(row):
        for j in range(col):
            dfs(i, j, 0)
            if len(res) != 0:
                return True
    return False
            

if __name__ == "__main__":
    # res = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    res = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    print(res)