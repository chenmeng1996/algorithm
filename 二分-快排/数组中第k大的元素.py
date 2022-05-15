
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    """
    使用快速排序的思想，但每次只需要快排大约一半的数组。

    或者使用小顶堆。
    """
    def quick_sort_once(nums, start, end) -> int:
        pivit = nums[start]
        i = start
        j = end
        reverse = False
        while i < j:
            if not reverse:
                while nums[j] < pivit:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    reverse = True
                    continue
            else:
                while nums[i] > pivit:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    reverse = False
                    continue
        return i
    target_index = k - 1
    start = 0
    end = len(nums) - 1
    while True:
        pivit_index = quick_sort_once(nums, start, end)
        if pivit_index == target_index:
            return nums[pivit_index]
        if pivit_index < target_index:
            # 在后半段寻找
            start = pivit_index + 1
        if pivit_index > target_index:
            # 在前半段寻找
            end = pivit_index - 1


if __name__ == "__main__":
    res = findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)
    print(res)