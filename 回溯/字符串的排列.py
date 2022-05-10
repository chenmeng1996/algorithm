from typing import List


def permutation(s: str) -> List[str]:
    visited = [False] * len(s)
    
    def helper(res: list, cur: list):
        _visited = set()
        for i in range(len(s)):
            if len(cur) == len(s):
                cur_s = "".join(cur)
                res.append(cur_s)
                return
            if visited[i] or (s[i] in _visited):
                continue
            cur.append(s[i])
            _visited.add(s[i])
            visited[i] = True
            helper(res, cur)
            cur.pop()
            visited[i] = False
        
    res = []
    cur = []
    helper(res, cur)
    return res
