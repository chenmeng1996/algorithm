

from typing import List

"""
https://leetcode-cn.com/problems/word-break/
"""
def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    动态规划。
    dp[i]表示以i结尾的字符串，是否可以由字典拼接而成。
    dp[i] = (s[0:i+1] in wordDict) or (dp[0] is True and s[1:i+1] in wordDict) or .... or (dp[i-1] is True and s[i:i+1] in wordDict)
    """
    wordSet = set()
    for word in wordDict:
        wordSet.add(word)
    dp = [False]*len(s)

    for i in range(len(s)):
        if s[:i+1] in wordSet:
            dp[i] = True
            continue
        for j in range(i):
            if dp[j] == False:
                continue
            if s[j+1:i+1] in wordSet:
                dp[i] = True
                break
    return dp[len(s)-1]


if __name__ == "__main__":
    res = wordBreak("leetcode", ["leet","code"])
    print(res)