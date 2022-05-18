

from collections import defaultdict, deque
from typing import List

"""
https://leetcode-cn.com/problems/course-schedule/

判断是否可能完成所有课程的学习？
"""
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    拓扑排序。

    1. 统计每个节点的出度节点(通过set保存该节点的入度节点) 和 每个节点的入度节点数量。
    2. 重复寻找入度为0的节点, 删除。并更新入度有该节点的节点入度。

    时间复杂度: O(节点数+边数)
    """
    # 统计每个节点的出度节点
    edges = defaultdict(set)
    for p in prerequisites:
        edges[p[1]].add(p[0])

    # 统计每个节点的入度数量
    in_nodes = [0] * numCourses
    for _, out_node_set in edges.items():
        for delete_node in out_node_set:
            in_nodes[delete_node] += 1

    # 课程学习顺序
    res = []
    # 广度优先遍历的队列
    que = deque()

    # 入度为0的节点加入队列
    for i in range(len(in_nodes)):
        if in_nodes[i] == 0:
            que.append(i)

    # 依次删除入度为0的节点, 并更新入度有该节点的节点入度数量。
    # 如果有该节点的入度变为0, 则也加入待删除列表。        
    while que:
        delete_node = que.popleft()
        res.append(delete_node)
        # 以该节点为头的节点的入度减1
        for node in edges[delete_node]:
            in_nodes[node] -= 1
            # 入度为0的节点加入队列
            if in_nodes[node] == 0:
                que.append(node)

    # 拓扑图有环            
    if len(res) != numCourses:
        return False
    return True


def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    广度优先搜索

    1. 构建邻接矩阵，表示有向图。
    2. 寻找起点，开始广度优先遍历。
    """
    pass

def canFinish3(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    深度优先搜索

    1. 构建邻接矩阵，表示有向图。
    2. 寻找起点，开始广度优先遍历。
    """
    pass

if __name__ == "__main__":
    res = canFinish(2, [[1,0]])
    print(res)