from collections import defaultdict, deque
from typing import List


"""
https://leetcode-cn.com/problems/course-schedule-ii/

返回任意一种课程学习顺序。
"""
def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        return []
    return res


def find_order_DFS(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    pass



def find_order_my(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    visited = []
    visited_set = set()
    deleted = [False] * len(prerequisites)

    # 寻找没有依赖的课程，并删除依赖该课程的依赖关系
    def check():
        has_prerequisites_course = set()
        for i in range(len(prerequisites)):
            if deleted[i]:
                continue
            has_prerequisites_course.add(prerequisites[i][0])
        no_prerequisites_course = []
        for i in range(numCourses):
            if i in visited_set:
                continue
            if i not in has_prerequisites_course:
                no_prerequisites_course.append(i)
        for v in no_prerequisites_course:
            for i in range(len(prerequisites)):
                if deleted[i]:
                    continue
                if prerequisites[i][1] == v:
                    deleted[i] = True
        return no_prerequisites_course

    while True:
        no_prerequisites_course = check()
        if len(no_prerequisites_course) == 0:
            return []
        for v in no_prerequisites_course:
            visited.append(v)
            visited_set.add(v)
        if len(visited) == numCourses:
            return visited
        

if __name__ == "__main__":
    res = find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    print(res)