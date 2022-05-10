
import functools
from typing import List


def minNumber(nums: List[int]) -> str:
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