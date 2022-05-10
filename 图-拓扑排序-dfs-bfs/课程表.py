"""
https://leetcode-cn.com/problems/course-schedule/
"""

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    拓扑排序。

    1. 统计每个节点的入度（通过set保存该节点的入度节点）
    2. 重复寻找入度为0的节点，删除。并更新入度有该节点的入度。
    """
    dic = {}
    for i in range(numCourses):
        dic[i] = set()
    for v in prerequisites:
        dic[v[0]].add(v[1])

    stack = []
    for k, v in dic.items():
        if len(v) == 0:
            stack.append(k)

    while stack:
        key = stack.pop()
        dic.pop(key)
        for k, v in dic.items():
            if key in v:
                v.remove(key)
                if len(v) == 0:
                    stack.append(k)
    
    return len(dic) == 0


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