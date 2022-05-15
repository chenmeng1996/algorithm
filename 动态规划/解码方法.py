from copy import copy


"""
https://leetcode-cn.com/problems/decode-ways/
"""

def numDecodings_count(s: str) -> int:
    """
    动态规划, dp[i]表示前i个字符的组合数.
    dp[i] = dp[i-1] + dp[i-2], 要注意一些条件:
    1. 如果s[i] == "0", 则不能加上dp[i-1]
    2. 如果s[i-1] == "0", 或者s[i-1:i+1], 则不能加上dp[i-2]
    """
    n = len(s)
    f = [1] + [0] * n
    for i in range(1, n + 1):
        if s[i - 1] != '0':
            f[i] += f[i - 1]
        if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
            f[i] += f[i - 2]
    return f[n]


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