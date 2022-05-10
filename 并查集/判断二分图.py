
from typing import List


"""
https://leetcode.cn/problems/is-graph-bipartite/
"""
def isBipartite(graph: List[List[int]]) -> bool:
    """
    并查集。
    二分图中, 选中一个顶点, 则该顶点之间相连的节点组成一个集合, 且顶点不在该集合中。
    遍历所有顶点, 都满足以上特性, 则是个二分图。
    """
    def find(node):
        if father[node] != node:
            father[node] = find(father[node])
        return father[node]

    def union(node1, node2):
        father[node1] = find(node2)

    nodes = len(graph)
    father = [node for node in range(nodes)]
    # 选择顶点
    for node in range(nodes):
        # 该顶点直接相连的节点
        for other in graph[node]:
            # 如果顶点和任意一个相连节点在一个集合中，则不是二分图
            if find(node) == find(other):
                return False
            # 如果顶点和相连节点不在一个集合，则把相连节点们加入到一个集合中
            union(other, graph[node][0])
    
    # 全部顶点都检查通过，是二分图
    return True

