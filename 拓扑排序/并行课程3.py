

from collections import defaultdict, deque
from typing import List


"""
https://leetcode.cn/problems/parallel-courses-iii/

time[i]表示完成第(i+1)门课程需要花费的 月份 数。

请你根据以下规则算出完成所有课程所需要的 最少 月份数：

1. 如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
2. 你可以 同时 上 任意门课程 。

请你返回完成所有课程所需要的 最少 月份数。
"""
def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    """
    拓扑排序 + 动态规划。

    dp[i] 表示完成第 i 门课程需要花费的最少月份数。
    dp[i] = time[i] + max(dp[j])，这里 j 是 i 的所有先修课程。
    设当前节点为v, 我们可以在计算出 dp[v]后, 更新dp[w]的所有先修课程耗时的最大值。
    这里 v 是 w 的先修课程。

    在拓扑排序时, 计算所有节点的dp值, 答案是dp的最大值。

    时间复杂度: O(n^2)
    空间复杂度: O()
    """
    # 统计每个先修课程的后修课程
    edge = defaultdict(set)
    for relation in relations:
        edge[relation[0]-1].add(relation[1]-1)

    # 统计每个课程的先修课程数
    in_nodes = [0]*n
    for _, node_set in edge.items():
        for node in node_set:
            in_nodes[node] += 1
    
    # 统计每个课程的最少花费时间
    dp = [0]*n
    
    # 拓扑排序，并更新课程的最少花费时间
    que = deque()
    for node in range(n):
        if in_nodes[node] == 0:
            que.append(node)
    while que:
        deleted_node = que.popleft()
        dp[deleted_node] += time[deleted_node]
        for node in edge[deleted_node]:
            in_nodes[node] -= 1
            dp[node] = max(dp[node], dp[deleted_node])
            if in_nodes[node] == 0:
                que.append(node)
    
    return max(dp)


if __name__ == "__main__":
    res = minimumTime(3, [[1,3],[2,3]], [3,2,5])
    print(res)