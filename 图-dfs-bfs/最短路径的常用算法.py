

"""
求两点之间的最短路径
"""
from copy import deepcopy
from typing import List


def dfs(grid: List[List[int]], start: int, end: int):
    """
    深度优先搜索
    """
    pass


"""
任意两点之间的最短距离
"""
def floyd(grid: List[List[int]]):
    """
    如果使用dfs, 需要遍历选择起点和终点, 使用n^2次dfs, 时间复杂度较高。

    floyd算法的时间复杂度是O(n^3)。
    """
    n = len(grid)
    # 最初两点之间的距离是直连的距离
    e = deepcopy(grid)
    # k是中转点, i和j是起点和终点。遍历所有中转点, 更新两点之间的最短距离
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if e[i][j] > e[i][k] + e[k][j]:
                    e[i][j] = e[i][k] + e[k][j]
    return e
            


"""
求某个节点到其他所有节点的最短距离。
"""
def dijkstra(grid: List[List[int]], start: int):
    """
    dijkstra算法。
    dijkstra算法基于贪心策略。每次新扩展一个路径最短的点, 更新与它相邻的所有点。
    """
    n = len(grid)
    # 源点到其他各点的最短距离
    dist = [0]*n
    # 记录点是否被访问
    visited = [False]*n
    # 用直连距离初始化dist
    for i in grid:
        dist[i] = grid[start][i]
    visited[start] = True
    # 遍历n-1次, 计算源点到其他节点的最短距离
    for _ in range(n-1):
        # 寻找源点到未访问节点的最短距离
        min_value = float("inf")
        target = 0
        for i in range(n):
            if i == start:
                continue
            if not visited[i] and dist[i] < min_value:
                min_value = dist[i]
                target = i
        # 未访问节点中离源点最短的节点作为target, 加入已访问集合
        visited[target] = True
        # 使用target作为中转节点, 计算target所有出边节点的最短距离
        for i in range(n):
            if i == start:
                continue
            if grid[target][i] > 0:
                if dist[i] > dist[target] + grid[target][i]:
                    dist[i] = dist[target] + grid[target][i]


"""
求某个节点到其他所有节点的最短距离。有负权边。
Dijkstra不能处理负权边。因为扩展到负权边的时候会产生更短的路径, 有可能破坏了已经更新的点路程不会改变的性质
"""
def bellman_ford(grid: List[List[int]], start: int):
    pass

"""
队列优化的Bellman-Ford。
只有那些在前一遍松弛中改变了最短路估计值的结点, 才可能引起它们邻接点最短路估计值发生改变。
"""
def SPFA(grid: List[List[int]], start: int):
    pass