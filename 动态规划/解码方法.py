from copy import copy


"""
https://leetcode-cn.com/problems/decode-ways/
"""

def numDecodings_count(s: str) -> int:
    """
    动态规划, dp[i]表示前i个字符的组合数.
    dp[i] = max(dp[i-1], dp[i-2]), 要注意一些条件
    """
    if len(s) == 0:
        return 0
    dp = [0]*len(s)
    for i in range(len(s)):
        if s[i] == "0":
            if i == 0 or s[i-1:i+1] == "00" or int(s[i-1:i+1]) > 26:
                return 0
        if i == 0:
            dp[i] = 1
        elif i == 1:
            if s[i] != "0":
                dp[i] = 1
            else:
                dp[i] = 0
            if int(s[i-1:i+1]) <= 26:
                dp[i] += 1
        else:
            if s[i] != "0":
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i] + dp[i-2]
    return dp[-1]


def numDecodings(s: str) -> int:
    """
    回溯
    """
    def helper(s: str, start, l: list, res: list):
        if start > len(s) - 1:
            res.append(copy(l))
            return
        if s[start] == "0":
            return
        for end in range(start, len(s)):
            if end - start > 1:
                break
            if end+1 <= len(s)-1 and s[end+1] == "0":
                continue
            if int(s[start:end+1]) > 26:
                break
            l.append(s[start:end+1])
            helper(s, end+1, l, res)
            l.pop()
    
    l = []
    res = []
    helper(s, 0, l, res)
    return len(res)


if __name__ == "__main__":
    res= numDecodings("11106")
    print(res)