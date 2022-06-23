from typing import List

"""
https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字。
"""
def majorityElement(nums: List[int]) -> int:
    """
    摩尔投票法。
    非众数和众数一一抵消，剩下来的元素是众数。
    """
    candidate = None
    count = 0
    for v in nums:
        if count == 0:
            candidate = v
            count += 1
        else:
            if candidate == v:
                count += 1
            else:
                count -= 1
    return candidate