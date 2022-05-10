
from copy import copy
from typing import List

"""
字符串分割成若干个子字符串，每个子字符串都是回文串。计算所有这种情况。
"""
def partition(s: str) -> List[List[str]]:
    """
    穷举所有分割情况，并判断每种情况是否是回文字符串。
    判断回文字符串会产生重复计算，所以先计算出来。
    dp[i][j]表示s[i,j]是否是回文串
    dp[i][j]是回文串，当且仅当dp[i+1][j-1]是回文串，且s[i]=s[j]
    """
    dp = [[True] * len(s) for _ in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            dp[i][j] = True if dp[i+1][j-1] and s[i] == s[j] else False
    

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
    
    res = []
    current_list = []
    permutation(s, 0, res, current_list)
    return res


if __name__ == "__main__":
    res = partition("aab")
    print(res)