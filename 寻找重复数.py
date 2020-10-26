from typing import List


def findDuplicate(nums: List[int]) -> int:
    n = len(nums) - 1
    # i为可能是重复的数字
    for i in range(1, n + 1):
        count = 0
        for j in nums:
            if i == j:
                count += 1
                if count > 1:
                    return i


if __name__ == '__main__':
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))