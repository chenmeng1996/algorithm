
from typing import Deque


def movingCount(m: int, n: int, k: int) -> int:
    """
    广度优先遍历
    """
    def check(a, b, k):
        _sum = 0
        for v in str(a):
            _sum += int(v)
        for v in str(b):
            _sum += int(v)
        if _sum > k:
            return False
        else:
            return True

    visited = [[False] * n for _ in range(m)]
    queue = Deque()
    queue.append((0, 0))
    count = 1
    visited[0][0] = True
    while queue:
        length = len(queue)
        for _ in range(length):
            i, j = queue.popleft()
            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i, new_j = i+x, j+y
                if new_i < 0 or new_i > m-1 or new_j < 0 or new_j > n-1:
                    continue
                if visited[new_i][new_j]:
                    continue
                if check(new_i, new_j, k):
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j))
                    count += 1
    return count


if __name__ == "__main__":
    res = movingCount(2, 3, 1)
    print(res)