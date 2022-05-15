from typing import List


"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    二分查找。TODO

    查找两个有序数组的中位数, 可以转换为查找两个有序数组中第k大的数。

    查找两个有序数组中第k大的数的思路:
    1. 比较两个数组的第k/2大的数(设是a和b)。
        1.1. 如果a<=b, 则a以及a之前的数都小于b, 而这些数的数量是k/2, 所以这些数不可能是第k大的数, 可以通过移动数组1的开始下标来“删除”这些数。
        1.2. 如果a>b, 同理, 通过移动数组2的开始下标来“删除”这些数。
    2. 删除不可能的数之后(设是c), 寻找的数变成第(k-c)个数。重复上述过程, 直到k=1或者有一个数组的元素都被“删除”。
    """
    def getKthElement(k):
        """寻找两个有序数组中的第k小的数"""
        # 两个数组的起始位置
        index1, index2 = 0, 0
        while True:
            # 数组1或数组2已经删完了，那么只能从剩下的数组中寻找
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            # 寻找两个数组最小的数，只要比较数组开头的元素即可
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 两个数组的第k/2大的数
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            # 比较两个数组的第k/2大的数，删除不可能是第k大的元素，更新k。
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1
    
    m, n = len(nums1), len(nums2)
    totalLength = m + n
    # 长度为奇数，中位数是第k小的数
    if totalLength % 2 == 1:
        return getKthElement((totalLength + 1) // 2)
    # 长度为偶数，中位数是第k小和第k+1小的两个数的平均数
    else:
        return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


if __name__ == "__main__":
    res = findMedianSortedArrays([1,3,4,9], [1,2,3,4,5,6,7,8,9])
    print(res)