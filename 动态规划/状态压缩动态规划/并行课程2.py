

from functools import lru_cache
from itertools import combinations
from typing import List


"""
https://leetcode.cn/problems/parallel-courses-ii/

一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了
"""
def minNumberOfSemesters(n: int, relations: List[List[int]], k: int) -> int:
    @lru_cache(None)
    def dfs(st):
        if st == (1<<n) -1:
            return 0
        res = float('inf')
        cands = [i for i in range(n) if not st&(1<<i) and dp[i]&st == dp[i]]
        for sub in combinations(cands, min(k, len(cands))):
            res = min(res, 1 + dfs(st|sum(1<<i for i in sub)))
        return res

    dp = [0]*n
    for x, y in relations:
        dp[y-1] |= 1<<(x-1)
    return dfs(0)