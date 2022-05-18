
from collections import defaultdict
from typing import List

"""
https://leetcode.cn/problems/possible-bipartition/
"""
def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    """
    dfs。
    使用染色法判断是否是二分图。
    """
    def dfs(node, color):
        # 起点已经上色，跳过
        if colors[node] != 0:
            return True
        colors[node] = color
        for other in dislikes_dic[node]:
            if colors[other] != 0 and colors[other] == color:
                return False
            if not dfs(other, -color):
                return False
        return True
        

    # 0表示未上色, -1表示上红色, 1表示上绿色
    colors = [0]*(n+1) 
    # 统计每个节点的相邻节点
    dislikes_dic = defaultdict(set)
    for dislike in dislikes:
        dislikes_dic[dislike[0]].add(dislike[1])
        dislikes_dic[dislike[1]].add(dislike[0])
    
    for node in range(1, n+1):
        if not dfs(node, -1):
            return False
    return True
