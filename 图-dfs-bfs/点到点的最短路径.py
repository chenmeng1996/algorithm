
from copy import copy
from typing import Deque, List


def bfs(matrix: List[List[int]], start: int, end: int) -> List[List[int]]:
    """
    表示无向图的方式是一个二维矩阵, 有权重
    """
    bfs()


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0],
    ]
    res = bfs(graph, 0, 3)
    print(res)
