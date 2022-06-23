
from typing import List


"""
https://leetcode.cn/problems/number-of-provinces/
"""
def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    并查集
    """
    def find(city):
        """寻找集合的根节点(代表）, 并进行路径压缩"""
        if parent[city] != city:
            parent[city] = find(parent[city])
        return parent[city]
    
    def union(city1, city2):
        """合并两个集合(集合1的代表的parent变成集合2的代表)"""
        parent[find(city1)] = find(city2)

    citys = len(isConnected)
    parent = [i for i in range(citys)]
    for city1 in range(len(isConnected)):
        for city2 in range(len(isConnected[0])):
            if isConnected[city1][city2]:
                union(city1, city2)
    
    # 遍历parent，寻找parent是自己的节点（即代表）的个数，这就是集合的个数
    res = 0
    for city in range(len(parent)):
        if parent[city] == city:
            res += 1
    return res