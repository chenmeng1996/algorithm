from collections import defaultdict
from typing import Deque, List


'''
https://leetcode-cn.com/problems/course-schedule-ii/

如果要求所有结果，怎么做？
'''

def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 有向无环图
    edges = defaultdict(list)
    for p in prerequisites:
        edges[p[1]].append(p[0])
    # 每个节点的入度
    in_nodes = [0] * numCourses
    for _, vs in edges.items():
        for v in vs:
            in_nodes[v] += 1
    # 节点序列
    res = []
    # 广度优先遍历
    que = Deque()
    for i in range(len(in_nodes)):
        if in_nodes[i] == 0:
            que.append(i)
    while que:
        node = que.popleft()
        res.append(node)
        # 去除该节点，以该节点为头的节点的入度减1
        for v in edges[node]:
            in_nodes[v] -= 1
            # 入度为0的节点加入队列
            if in_nodes[v] == 0:
                que.append(v)
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