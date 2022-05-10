

import collections
from typing import List

"""
https://leetcode-cn.com/problems/open-the-lock/
"""
def openLock(deadends: List[str], target: str) -> int:
    """
    bfs。
    从"0000"开始bfs搜索，直到搜索到target。
    """
    que = collections.deque()
    que.append("0000")
    s = set(deadends)
    visited = set()
    visited.add("0000")
    count = -1
    
    while que:
        count += 1
        for _ in range(len(que)):
            x = que.popleft()
            if x in s:
                continue
            if x == target:
                return count
            for i in range(4):
                for j in [-1,1]:
                    a = int(x[i])
                    a += j
                    if a == -1:
                        a = 9
                    if a == 10:
                        a = 0
                    new_x = x[:i]+str(a)+x[i+1:]
                    if new_x not in s and new_x not in visited:
                        que.append(new_x)
                        visited.add(new_x)
    return -1
        
        
if __name__ == "__main__":
    res = openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888")
    print(res)