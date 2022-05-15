

from typing import List

"""
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
"""
def reversePairs(nums: List[int]) -> int:
    """
    归并排序。
    在合并两个有序数组(设数组1和数组2)时, 如果选择合并数组2的某个数字, 则证明该数字比数组1的所有数字都小, 则逆序对个数增加数组1的当前长度。
    """
    def merge(nums, start1, end1, start2, end2, counter):
        new_nums = []
        i = start1
        j = start2
        while i <= end1 and j <= end2:
            if nums[i] <= nums[j]:
                new_nums.append(nums[i])
                i += 1
            else:
                new_nums.append(nums[j])
                j += 1
                counter[0] = counter[0] + (end1 - i + 1)
        if i <= end1:
            new_nums.extend(nums[i:end1+1])
        if j <= end2:
            new_nums.extend(nums[j:end2+1])
        nums[start1:end2+1] = new_nums
    
    def sort(nums, start, end, counter):
        if start >= end:
            return
        mid = (start + end) // 2
        sort(nums, start, mid, counter)
        sort(nums, mid+1, end, counter)
        merge(nums, start, mid, mid+1, end, counter)
    
    counter = [0]
    sort(nums, 0, len(nums)-1, counter)
    return counter[0]
    

if __name__ == "__main__":
    res = reversePairs([7,5,6,4])
    print(res)