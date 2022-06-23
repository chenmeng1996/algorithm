
from typing import List


"""
https://leetcode.cn/problems/is-graph-bipartite/
"""
def isBipartite(graph: List[List[int]]) -> bool:
    """
    dfs。
    选择一个起点进行dfs遍历。 将第一个节点染成红色。 与第一个节点相连的节点染成相反颜色（绿色）。绿色节点相连的节点染成红色。
    如果全部节点都染色成功, 则是一个二分图。如果在染色时, 发现已经被染色了且与预期颜色不同, 则不是二分图。

    因为图不一定是连通图, 所以需要遍历每个起点。


    bfs和并查集也可以解决。
    """
    def dfs(index, color):
        # 起点已经访问过，跳过
        if colors[index] != 0:
            return True
        # 上颜色
        colors[index] = color
        for target in graph[index]:
            # 应该要上相反颜色的节点已经被染上不是预期的颜色，失败
            if colors[target] != 0 and colors[target] == color:
                return False
            # 下一个节点上相反颜色
            if not dfs(target, -color):
                return False
        return True


    n = len(graph)
    # 节点颜色，0是未上色，-1是红色，1是绿色
    colors = [0] * n
    for start in range(n):
        if not dfs(start, -1):
            return False
    return True
