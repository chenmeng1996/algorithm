from typing import List


def findMedianSortedArrays_1(nums1: List[int], nums2: List[int]) -> float:
    """
    思路：归并排序的归并思路，将两个有序数组合并成一个有序数组。
    分别从头开始遍历两个数组，一一对比，遍历（m + n）/ 2个元素即可找到中位数
    :param nums1:
    :param nums2:
    :return:
    """
    length = len(nums1) + len(nums2)
    target = length // 2 + 1
    count = 0
    i, j = 0, 0

    candidate = []
    while True:
        if i == len(nums1):
            m = nums2[j]
            j += 1
        elif j == len(nums2):
            m = nums1[i]
            i += 1
        elif nums1[i] <= nums2[j]:
            m = nums1[i]
            i += 1
        else:
            m = nums2[j]
            j += 1
        count += 1
        if count == target - 1 or count == target:
            candidate.append(m)
            if count == target:
                break
    if length % 2 == 0:
        return (candidate[0] + candidate[1]) / 2
    else:
        return candidate[0] if len(candidate) == 1 else candidate[1]

def findMedianSortedArrays_2(nums1: List[int], nums2: List[int]) -> float:
    import sys
    """
    二分查找，O(log(m+n))，找到数组的两个分割线，使得左右分成两个数组a1和a2。
    分割线满足以下条件：
    1.len(a1) = len(a2)或者 len(a1) = len(a2)+1
    2.a1最大的元素小于a2最小的元素
    :param nums1:
    :param nums2:
    :return:
    """
    # 短数组在前，长数组在后，方便
    if len(nums1) > len(nums2):
        tmp = nums1
        nums1 = nums2
        nums2 = tmp
    m = len(nums1)
    n = len(nums2)
    # 分割线左边的元素个数，满足了奇数和偶数
    total_left = (m + n + 1) // 2

    # 在num1的[0, m]区间内查找分割线, i，j分别为nums1，nums2分割线右边元素
    # 使得nums1[i-1] < nums2[j] and nums1[i] > nums2[j-1]
    left, right = 0, m
    while left < right:
        # 二分
        i = left + (right - left + 1) // 2 # 中位数加1，避免i-1越界 #TODO
        j = total_left - i
        if nums1[i-1] > nums2[j]:
            # nums1分割线元素太大，往左去一点，在nums1的[left, i-1]
            right = i - 1
        else:
            # nums1分割线元素比较小了，往右看能不能找个大一点的
            left = i

    i = left
    j = total_left - i
    nums1_left_max = nums1[i-1] if i > 0 else float('-inf')
    nums1_right_min = nums1[i] if i < m else float('inf')
    nums2_left_max = nums2[j - 1] if j > 0 else float('-inf')
    nums2_right_min = nums2[j] if j < n else float('inf')

    if (m + n) % 2 == 0:
        return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
    else:
        return max(nums1_left_max, nums2_left_max)

print(findMedianSortedArrays_1([1, 3], [2]))
print(findMedianSortedArrays_2([1, 3], [2]))
