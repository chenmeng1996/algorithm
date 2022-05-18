
from typing import List


"""
https://leetcode.cn/problems/word-search/
"""
def exist(board: List[List[str]], word: str) -> bool:
    """
    dfs。
    遍历每个点作为起点，进行dfs。
    """
    def dfs(i, j, visited, word, index):
        if board[i][j] != word[index]:
            return False
        visited[i][j] = True
        if index == len(word) - 1:
            return True
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_i = i + x
            next_j = j + y
            if next_i < 0 or next_i > len(board) - 1 or next_j < 0 or next_j > len(board[0]) - 1:
                continue
            if visited[next_i][next_j]:
                continue
            if dfs(next_i, next_j, visited, word, index+1):
                return True
        visited[i][j] = False
        return False
    
    if len(board) == 0:
        return False
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, visited, word, 0):
                return True
    return False


if __name__ == "__main__":
    res = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print(res)