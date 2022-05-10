
from copy import copy
from typing import Deque, List


"""
表示无向图的方式是一个二维矩阵
"""
def dfs(matrix: List[List[int]], start: int, end: int) -> List[List[int]]:
    """
    dfs
    """
    res = []
    visited = [False] * len(matrix)
    path = []

    def fn(start):
        for i in range(len(matrix)):
            if matrix[start][i] == 0 or visited[i]:
                continue
            path.append(i)
            visited[i] = True
            if i == end:
                res.append(copy(path))
                visited[i] = False
                path.pop()
                break
            fn(i)
            visited[i] = False
            path.pop()
    
    path.append(start)
    visited[start] = True
    fn(start)
    return res


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0],
    ]
    res = dfs(graph, 0, 3)
    print(res)
