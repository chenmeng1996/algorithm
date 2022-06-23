from typing import List

'''
给你一个包含 n 个整数的数组 nums,判断nums中是否存在三个元素 a,b,c,使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
'''
def three_sum(nums: List[int]) -> List[List[int]]:
    '''
    排序,a<b<c,遍历a,双指针寻找b和c
    '''
    nums.sort()
    res = []
    i = 0
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if j > i+1 and nums[j] == nums[j-1]:
                j += 1
                continue
            s = nums[j] + nums[k]
            if s == target:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif s < target:
                j += 1
            elif s > target:
                k -= 1
    return res


if __name__ == "__main__":
    res = three_sum([-1,0,1,2,-1,-4])
    print(res)