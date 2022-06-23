
'''
给你两个单词 word1 和 word2,请返回将 word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
'''
import functools
from queue import Empty


"""
https://leetcode.cn/problems/edit-distance/

给你两个单词 word1 和 word2,请返回将 word1转换成word2 所使用的最少操作数。

你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""
def min_distance(s1: str, s2: str) -> int:
    """
    二维动态规划

    dp[i][j]表示s1[0:i]转换成s2[0:j]的最少操作数。
    如果s1[i-1] = s2[j-1], 则dp[i][j] = dp[i-1][j-1]
    如果s1[i-1] != s2[j-1], 则dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    dp[i-1][j-1] 表示替换操作, dp[i-1][j]表示删除操作, dp[i][j-1]表示插入操作。

    时间复杂度: O(mn)
    空间复杂度: O(mn)
    """
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        dp[i][0] = i
    for j in range(1, len(s1)+1):
        dp[0][j] = j
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]



def min_distance_3(s1: str, s2: str) -> int:
    """
    dfs回溯 + 备忘录
    """
    @functools.lru_cache(None)
    def dfs(s1, s2):
        """返回使s1和s2相同的操作数"""
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)
        # 从第一个字符开始比较
        if s1[0] == s2[0]:
            return dfs(s1[1:], s2[1:])
        # 第一个字符不一样，有三种操作情况，都试一下
        # 替换字符
        replace_choice = 1 + dfs(s1[1:], s2[1:])
        # 删除字符
        delete_choice = 1 + dfs(s1[1:], s2[:])
        # 增加字符
        add_choice = 1 + dfs(s1[:], s2[1:])
        return min(replace_choice, delete_choice, add_choice)
    return dfs(s1, s2)
            

if __name__ == "__main__":
    # res = min_distance("horse", "ros")
    # res = min_distance_2("intention", "execution")
    res = min_distance_3("sea", "eat")
    print(res)