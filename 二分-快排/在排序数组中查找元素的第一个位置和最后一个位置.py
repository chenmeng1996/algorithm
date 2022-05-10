
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    """
    二分查找 
    时间复杂度: logN
    """
    start = 0
    end = len(nums) - 1
    while start <= end and start >= 0 and end < len(nums):
        middle = (start + end) // 2
        if nums[middle] == target:
            # 往前找
            first = middle
            for i in range(middle-1, -1, -1):
                if nums[i] == target:
                    first = i
                else:
                    break
            # 往后找
            last = middle
            for i in range(middle+1, len(nums)):
                if nums[i] == target:
                    last = i
                else:
                    break
            return [first, last]
        elif nums[middle] < target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle - 1
    return [-1, -1]


if __name__ == "__main__":
    res = searchRange(nums = [1], target = 1)
    print(res)