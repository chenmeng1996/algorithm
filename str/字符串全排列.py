
from copy import deepcopy
from operator import le
from typing import List


'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''
def permute(nums: List[int]) -> List[List[int]]:
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
