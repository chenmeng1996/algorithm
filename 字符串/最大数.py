
import functools
from typing import List

"""
https://leetcode.cn/problems/largest-number/
"""
def largestNumber(nums: List[int]) -> str:
    """
    数字转换成字符串，并排序。
    两个字符串数字的排序规则为: 如果s1+s2 > s2+s1, 则s1 > s2, 否则s1 < s2。
    """
    def compare(x, y):
        a = x + y
        b = y + x
        if a >= b:
            return 1
        else:
            return -1

    nums_str = [str(v) for v in nums]
    nums_str.sort(key=functools.cmp_to_key(compare), reverse=True)
    res = "".join(nums_str)
    if res[0] == "0":
        return "0"
    else:
        return res