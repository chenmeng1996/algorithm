
import functools
from typing import List

"""
https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
"""
def minNumber(nums: List[int]) -> str:
    """
    数字转换成字符串，并排序。
    两个字符串数字的排序规则为: 如果s1+s2 > s2+s1, 则s1 > s2, 否则s1 < s2。
    """
    def compare(x, y):
        a = x + y
        b = y + x
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    nums_str = [str(v) for v in nums]
    nums_str.sort(key=functools.cmp_to_key(compare))
    return "".join(nums_str)


if __name__ == "__main__":
    res = minNumber([824,938,1399,5607,6973,5703,9609,4398,8247])
    print(res)