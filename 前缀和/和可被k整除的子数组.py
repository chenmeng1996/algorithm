
from collections import defaultdict
from typing import List

"""
https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
"""
def subarraysDivByK(nums: List[int], k: int) -> int:
    """
    同余定理，如果a%c == b%c，则(a-b)%c==0。
    
    nums[i:j] % k == 0
    即(pre[j] - pre[i]) % k == 0，
    即 pre[j] % k == pre[i] % k

    所以为了快速找到符合条件的pre个数，哈希表的key应该存储pre对k的模。
    """
    cache = defaultdict(int)
    cache[0] = 1
    pre = 0
    count = 0
    for v in nums:
        pre += v
        module = pre % k
        count += cache[module]
        cache[module] += 1
    return count
        