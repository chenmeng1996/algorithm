
from collections import deque
from typing import List


"""
https://leetcode.cn/problems/number-of-provinces/
"""
def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    dfs 计算图的连通分量数

    时间复杂度 O(n^2)
    空间复杂度 O(n)
    """
    def dfs(city):
        visited[city] = True
        for target in range(citys):
            if isConnected[city][target]:
                if visited[target]:
                    continue
                dfs(target)

    citys = len(isConnected)
    visited = [False] * citys
    res = 0
    for city in range(citys):
        if visited[city]:
            continue
        dfs(city)
        res += 1
    return res


def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    bfs 计算图的连通分量数
    """
    citys = len(isConnected)
    visited = [False] * citys
    res = 0
    for city in range(citys):
        if visited[city]:
            continue
        res += 1
        queue = deque()
        queue.append(city)
        while queue:
            cur = queue.popleft()
            for target in range(citys):
                if isConnected[cur][target]:
                    if visited[target]:
                        continue
                    visited[target] = True
                    queue.append(target)
    return res