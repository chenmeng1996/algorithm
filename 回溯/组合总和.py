
import copy
from typing import List

"""
https://leetcode-cn.com/problems/combination-sum/


candidates中每个数字可以无限次使用。
"""
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    回溯。先对candidates排序。回溯时，后一个数字不能比前一个数字小。
    """
    def helper(canditates, index, res, path, total):
        for i in range(index, len(candidates)):
            v = candidates[i]
            total += v
            path.append(v)
            if total == target:
                res.append(copy.deepcopy(path))
                total -= v
                path.pop()
                return
            elif total > target:
                total -= v
                path.pop()
                return
            else:
                helper(canditates, i, res, path, total)
                total -= v
                path.pop()

    candidates.sort()
    res = []
    path = []
    helper(candidates, 0, res, path, 0)
    return res


if __name__ == "__main__":
    res = combinationSum([2,3,5], 8)
    print(res)