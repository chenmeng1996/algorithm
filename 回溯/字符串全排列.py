
from copy import deepcopy
from operator import le
from typing import List


"""
https://leetcode-cn.com/problems/permutations/
"""
def permute(nums: List[int]) -> List[List[int]]:
    """
    递归实现n层for循环嵌套, 维护一个已访问数组, 记录每个元素是否被使用
    维护一个当前list, 记录一种情况
    """
    def permute_helper(nums, visited: List[bool], res: list, cache: list):
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            cache.append(nums[i])
            permute_helper(nums, visited, res, cache)
            visited[i] = False
            cache.pop()
        if len(cache) == len(nums):
            cl = deepcopy(cache)
            res.append(cl)
        return
    
    visited = [False] * len(nums)
    res = []
    cache = []
    permute_helper(nums, visited, res, cache)
    return res


if __name__ == "__main__":
    res = permute([1, 2, 3])
    print(res)
