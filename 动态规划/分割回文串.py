
from copy import copy
from typing import List

"""
https://leetcode.cn/problems/palindrome-partitioning/
"""
def partition(s: str) -> List[List[str]]:
    """
    动态规划计算所有的回文字串: 
    dp[i][j]表示s[i,j]是否是回文串
    dp[i][j]是回文串, 当且仅当dp[i+1][j-1]是回文串,且s[i]=s[j]。
    从右往左遍历i, 从左往右遍历j。

    回溯法穷举所有分割情况，并判断每种情况是否是回文字符串。
    """
    def permutation(s, start, res: list, current_list: list):
        if start >= len(s):
            return
        for i in range(start, len(s)):
            if dp[start][i]:
                current_list.append(s[start:i+1])
                if i == len(s) - 1:
                    res.append(copy(current_list))
                permutation(s, i+1, res, current_list)
                current_list.pop()
    

    dp = [[True] * len(s) for _ in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    res = []
    current_list = []
    permutation(s, 0, res, current_list)
    return res


if __name__ == "__main__":
    res = partition("aab")
    print(res)