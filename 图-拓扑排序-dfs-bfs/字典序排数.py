
from typing import List

"""
https://leetcode-cn.com/problems/lexicographical-numbers/
"""
def lexicalOrder(n: int) -> List[int]:
    """
    dfs。
    """
    def dfs(start, end, res):
        for i in range(start, end+1):
            if i > n:
                break
            res.append(i)
            dfs(i*10, i*10+9, res)
    res = []
    dfs(1, 9, res)
    return res

def lexicalOrder_1(n: int) -> List[int]:
    """
    要求空间复杂度O(1)，使用dfs非递归。
    dfs非递归一般是使用栈，但是空间复杂度不是O(1)。
    TODO 很精妙，需要反复琢磨
    """
    res = [0]*n
    num = 1
    for i in range(n):
        res[i] = num
        if num * 10 <= n:
            # 可以继续dfs
            num *= 10
        else:
            # 不能继续dfs，那么在当前dfs推进num：num += 1
            # 如果推进不了num，那么需要返回dfs。推进不了num有两种情况，一是末尾遍历到9了。二是数字超过n了。
            # 返回dfs，需要恢复num。恢复num通过num //= 10
            while num % 10 == 9 or num + 1 > n:
                num //= 10
            num += 1
    return res