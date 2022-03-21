from typing import List


'''
https://leetcode-cn.com/problems/next-permutation/

整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
'''
def next_permutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    swap_index = None
    for i in range(len(nums)-2, -1, -1):
        if swap_index is not None:
            break
        for j in range(len(nums)-1, i, -1):
            if nums[i] < nums[j]:
                swap_index = i
                nums[i], nums[j] = nums[j], nums[i]
                break
    # 对swap_index之后的数组做排序
    if swap_index == None:
        swap_index = -1
    def bubble_sort(nums: List[int], start):
        for i in range(start, len(nums)-1):
            finished = True
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    finished = False
            if finished:
                return
    bubble_sort(nums, swap_index+1)


if __name__ == "__main__":
    nums = [1,2,3]
    next_permutation(nums)
    print(nums)