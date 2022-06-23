from typing import List
from unittest import result
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    
    return res
def twoSum(nums: List[int], target: int) -> List[int]:
    new_nums=sorted(nums)
    # nums.sort()
    i=0
    j=len(nums)-1
    res=[]
    while i<j:
        sum=new_nums[i]+new_nums[j]
        if sum>target:
            j-=1
        elif sum<target:
            i+=1
        else:
            #sum==target
            res.append(new_nums[i])
            res.append(new_nums[j])
            break
    # k=0
    res2=[]
    for k in range(len(nums)):
        if nums[k] in res:
            res2.append(k)  
    return res2

if __name__ == '__main__':
    res = twoSum([4,7,2,11], 9)
    print(res)



