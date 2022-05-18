
from collections import deque
from typing import List


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    广度优先遍历
    """
    if grid[0][0] == 1:
        return -1
    if len(grid) == 1:
        return 1
    length = len(grid)
    queue = deque()
    visited = {}
    queue.append((0, 0))
    visited[(0, 0)] = True
    count = 1
    while len(queue) != 0:
        # 当前层的位置个数
        l = len(queue)
        for _ in range(l):
            # 当前层的位置个数都作为当前位置，走一下广度遍历
            i, j = queue.popleft()
            # 当前位置的下一步的所有位置都走一下（广度遍历）
            for pos_i, pos_j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1, -1), (1,0), (1,1)]:
                next_i = i + pos_i
                next_j = j + pos_j
                # 下一步的坐标合法 且是连通的 且没有访问过
                if 0 <= next_i < length and 0 <= next_j < length \
                    and grid[next_i][next_j] == 0 and (next_i, next_j) not in visited:
                    # 是否到了目标位置
                    if next_i == length - 1 and next_j == length - 1:
                        return count + 1
                    queue.append((next_i, next_j))
                    visited[(next_i, next_j)] = True
        # 当前层的位置都走了下一步，步数加1。不用考虑当前层没有下一步，因为没有下一步，队列没有新元素加入，变为空
        count += 1
    # 全部走完了，也没走到目标位置
    return -1


if __name__ == "__main__":
    res = shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]])
    print(res)