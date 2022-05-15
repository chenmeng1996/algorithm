

"""
https://leetcode.cn/problems/longest-common-subsequence/
"""
def longest_common_subsequence(s1: str, s2: str):
    """
    二维动态规划。

    dp[i][j]表示s1[0:i]和s2[0:j]的最长公共子序列长度
    如果s1[i-1] = s2[j-1], 则dp[i][j] = dp[i-1][j-1] + 1
    如果s1[i-1] != s2[j-1], 则dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    dp[0][j] = 0
    dp[i][0] = 0

    思路解析：
    1. 如果s1[i-1] = s2[j-1]。这个没什么好讲的, 最后一个字符相等, 长度加1即可。
    2. 如果s1[i-1] != s2[j-1]。最后一个字符不相等, 但是有两种情况：
        2.1 s1最后一个字符可能与s2中某个字符相等, 这种情况下计算dp[i][j-1] (内部已经递归进行计算了)。
        2.2 s2最后一个字符可能与s1中某个字符相等, 这种情况下计算dp[i-1][j]
    """
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    res = longest_common_subsequence("abcde", "ace")
    print(res)