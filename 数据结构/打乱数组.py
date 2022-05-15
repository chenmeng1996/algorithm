
import copy
import random
from typing import List

"""
https://leetcode-cn.com/problems/shuffle-an-array/solution/
"""
class Solution:
    """
    洗牌算法。
    
    在删除下标为i的元素时，可以先将下标为i的元素与最后一个元素交换位置，然后再删除最后一个元素。
    可以将删除元素的时间复杂度从O(n)变为O(1).
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy_nums = copy.deepcopy(self.nums)

    def reset(self) -> List[int]:
        self.nums[:] = self.copy_nums
        return self.nums

    def shuffle(self) -> List[int]:
        self.reset()
        res = []
        n = len(self.nums) - 1
        for _ in range(len(self.nums)):
            i = random.randint(0, n)
            res.append(self.nums[i])
            self.nums.pop(i)
            n -= 1
        return res
            



if __name__ == "__main__":
    obj = Solution([1,2,3,4])
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)