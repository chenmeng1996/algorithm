
from copy import deepcopy
from operator import le
from typing import List


'''
给定一个可能含重复数字的数组 nums ，返回其 所有可能的不重复的全排列 。你可以 按任意顺序 返回答案。
'''
def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    先排序。

    递归实现n层for循环嵌套, 如果当前元素和前一个元素相同, 则跳过
    维护一个已访问数组, 记录每个元素是否被使用
    维护一个当前list, 记录一种情况
    """
    def permute_helper(nums, visited: List[bool], res: list, cache: list):
        currentVisited = set()
        for i in range(len(nums)):
            if visited[i] or nums[i] in currentVisited:
                continue
            visited[i] = True
            currentVisited.add(nums[i])
            cache.append(nums[i])
            permute_helper(nums, visited, res, cache)
            visited[i] = False
            cache.pop()
        if len(cache) == len(nums):
            cl = deepcopy(cache)
            res.append(cl)
        return
    
    sorted(nums)
    visited = [False] * len(nums)
    res = []
    cache = []
    permute_helper(nums, visited, res, cache)
    return res


if __name__ == "__main__":
    res = permute_unique([1,1,2])
    print(res)
