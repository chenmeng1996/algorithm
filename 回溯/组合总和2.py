from typing import List
import copy


"""
https://leetcode-cn.com/problems/combination-sum-ii/

candidates中的每个数字在每个组合中只能使用一次。

变种：如果每个数字可以使用两次呢？
"""


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    注意跳过重复数字
    """
    def helper(candidates, start, res, cur, total):
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            v = candidates[i]
            cur.append(v)
            total += v
            if total == target:
                res.append(copy.deepcopy(cur))
                cur.pop()
                total -= v
                break
            elif total > target:
                cur.pop()
                total -= v
                break
            else:
                helper(candidates, i+1, res, cur, total)
                cur.pop()
                total -= v
    
    res = []
    cur = []
    candidates.sort()
    helper(candidates, 0, res, cur, 0)
    return res