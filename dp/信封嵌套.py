

import functools
from typing import List



def max_envelopes(envelopes: List[List[int]]) -> int:
    """
    先按照信封长度升序排序, 保证长度递增满足嵌套需求。
    再将长度相同的信封, 按照宽度降序排序。目的是在代入最长递增子序列时, 不会重复选择两个长度相同的信封。
    """
    def compare(x, y):
        if x[0] != y[0]:
            return 1 if x[0] > y[0] else -1
        if x[1] < y[1]:
            return 1
        elif x[1] > y[1]:
            return -1
        else:
            return 0

    # envelopes.sort(key=functools.cmp_to_key(compare))
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    nums = []
    for v in envelopes:
        nums.append(v[1])
    return length_of_LIS(nums)

def length_of_LIS(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        max_len = 1
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] + 1 > max_len:
                max_len = dp[j] + 1
        dp[i] = max_len
    return max(dp)
    

if __name__ == "__main__":
    res = max_envelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])
    print(res)