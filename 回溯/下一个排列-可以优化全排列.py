from typing import List


"""
https://leetcode-cn.com/problems/next-permutation/
"""
def next_permutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    从右往左寻找，找到第一个元素（这个元素比右边的元素小）。
    此时该元素右边的元素是降序的（从左往右），从右往左找到第一个比该元素大的元素，交换之。交换后右边依然是降序的，所以通过反转数组可以变成升序。
    """
    # 找swap元素
    swap_index = None
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            swap_index = i
            break

    # 没找到，即整个数组是降序的（已经是最大数了），需要返回最小数（反转数组）
    if swap_index is None:
        return nums.reverse()
    
    # 找到交换元素，与右边数组（降序的）比交换元素大的最小元素交换位置
    for i in range(len(nums)-1, swap_index, -1):
        if nums[i] > nums[swap_index]:
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            break
    
    # 可以证明交换后，右边的数组依然是降序的，所以对右边数组的升序操作可以变为反转数组
    i = swap_index + 1
    j = len(nums)-1
    while i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        

if __name__ == "__main__":
    nums = [1,2,3]
    next_permutation(nums)
    print(nums)