

import bisect
import functools
from typing import List


"""
https://leetcode.cn/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
"""
def max_envelopes(envelopes: List[List[int]]) -> int:
    """
    先按照信封长度升序排序, 保证长度递增满足嵌套需求。
    再将长度相同的信封, 按照宽度降序排序。目的是在代入最长递增子序列时, 不会重复选择两个长度相同的信封。

    时间复杂度O(nlogn)
    """
    def compare(x, y):
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        elif x[1] < y[1]:
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
    """
    贪心 + 二分查找  时间复杂度O(nlogn)

    贪心思想：如果要使上升子序列尽可能长，则我们需要使序列上升的尽可能慢，因此希望在每次序列尾部增加的元素尽可能小。

    时间复杂度: O(nlogn)
    """
    d = []
    for v in nums:
        if len(d) == 0 or v > d[-1]:
            d.append(v)
        else:
            index = bisect.bisect_left(d, v)
            d[index] = v
    return len(d)
    

if __name__ == "__main__":
    res = max_envelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])
    print(res)