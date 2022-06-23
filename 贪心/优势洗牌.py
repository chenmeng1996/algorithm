

from collections import defaultdict
from typing import List


"""
https://leetcode.cn/problems/advantage-shuffle/
"""
def advantageCount(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    贪心: 让nums1[i]比nums2[i]大, 但是尽可能让nums1[i]小。

    两个数组排序。
    遍历nums1, 每次取最小值:
    1. 如果最小值比nums2的最小值大, 则形成对应关系, nums2的左指针右移。
    2. 如果最小值比nums2的最小值小, 则最小值没用了, 先记录, 后面可以随机对应(反正也是数)。

    所以要有哈希表, 记录对应关系, 以及nums1中没用的数据。
    """
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2)

    # 记录nums2中的元素和nums1元素的对应关系
    # 因为可能有重复元素, 所以有数组
    pair = defaultdict(list)
    # 记录nums1中没用的数
    not_used = []

    i = 0
    for v in sorted_nums1:
        if v > sorted_nums2[i]:
            pair[sorted_nums2[i]].append(v)
            i += 1
        else:
            not_used.append(v)
    
    # 根据记录，构造结果
    res = []
    for v in nums2:
        p = pair[v]
        # 有优势对
        if len(p) > 0:
            res.append(p.pop())
        # 没有优势对, 从没用的数中随便取一个
        else:
            res.append(not_used.pop())
    return res

