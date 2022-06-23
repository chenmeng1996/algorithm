import functools
from typing import List
def lengthOfLIS(nums: List[int]) -> int:
    # sub_nums=[]
    if len(nums)<=0:
        return 0
    dp=[1]*len(nums)
    # dp=[[1]*len(nums) for _ in range]
    for i in range(len(nums)):      
        for j in range(i):
            if nums[i]> nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text1)<=0 or len(text2)<=0:
        return 0
    dp=[[1]*len(text2) for _ in range(len(text1))]
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i]==text2[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[len(text1)-1][len(text2)-1]


        
def maxEnvelopes(envelopes: List[List[int]]) -> int:
    def compare(x, y):
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        elif x[0] == y[0]:
            if x[1] > y[1]:
                return 1
            elif x[1] < y[1]:
                return -1
            else:
                return 0
    envelopes.sort(key=functools.cmp_to_key(compare))
    dp=[1]*len(envelopes)
    for i in range(len(envelopes)):      
        for j in range(i):
            if envelopes[i][0]> envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
if __name__ == '__main__':
    res = longestCommonSubsequence("abde","ade")
    res2 = maxEnvelopes([[2,1],[4,4],[4,3],[3,8]])
    print(res2)

