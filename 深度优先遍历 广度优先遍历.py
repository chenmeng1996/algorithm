import queue
from typing import List, Dict


def bfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """
    广度优先遍历，核心思想是
    1. 利用队列保存访问顺序
    2. 利用set记录访问过的节点
    """
    res = []
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        res.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
    return res


def bfs_2(aa: List[List[int]], start: int) -> List[int]:
    """
    表示有向五环图的方式是一个二维矩阵
    """
    res = []
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        res.append(u)
        for v in range(len(aa[u])):
            if v != u and aa[u][v] == 1 and v not in visited:
                q.put(v)
                visited.add(v)
    return res


def dfs(adj: Dict[int, List[int]], start: int) -> List[int]:
    """
    深度优先遍历，核心思想是：
    1. 用栈记录访问父节点的访问顺序
    2. 用set记录访问过的节点
    """
    res = []
    visited = set()
    stack = []
    stack.append(start)
    res.append(start)
    while stack:
        top = stack[-1]
        if top not in adj:
            stack.pop()
            continue
        all_visited = True
        for v in adj[top]:  # 这个地方，可以优化，已经访问过的节点不必再访问
            if v not in visited:
                stack.append(v)
                visited.add(v)
                res.append(v)
                all_visited = False
                break
        if all_visited:
            stack.pop()
    return res


def dfs_optimize(adj: Dict[int, List[int]], start: int) -> List[int]:
    """
    对dfs的优化，栈记录了父节点和子节点的索引，避免多次遍历一个父节点的所有子节点
    """
    res = []
    visited = set()
    stack = [[start, 0]]
    res.append(start)
    while stack:
        v, next_child_idx = stack[-1]
        if v not in adj or next_child_idx >= len(adj[v]):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        res.append(next_child)
        stack.append([next_child, 0])
    return res


if __name__ == "__main__":
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    print("bfs", bfs(graph, 1))
    print("dfs", dfs(graph, 1))
    print("dfs_optimize", dfs_optimize(graph, 1))

    graph_2 = [
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    print(bfs_2(graph_2, 0))