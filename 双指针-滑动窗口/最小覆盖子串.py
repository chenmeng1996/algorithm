
"""
https://leetcode.cn/problems/minimum-window-substring/
"""
from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    """
    滑动窗口。
    哈希表存储目标字符串的字符和个数。
    在滑动窗口时, 用哈希表维护当前窗口的目标字符个数。
    """
    t_dic = defaultdict(int)
    for c in t:
        t_dic[c] += 1
    
    res = [0, len(s)]
    s_dic = defaultdict(int)
    l = r = 0
    while r < len(s):
        if s[r] in t_dic:
            # 目标字符数量加1
            s_dic[s[r]] += 1
            # 尝试移动左边窗口，减少目标字符
            while True:
                # 不是目标字符，可以删除
                if s[l] not in t_dic:
                    l += 1
                else:
                    # 是目标字符，且超了，可以删除
                    if s_dic[s[l]] > t_dic[s[l]]:
                        s_dic[s[l]] -= 1
                        l += 1
                    # 是目标字符，没超，不可以删除
                    else:
                        break
            # 当前窗口是否满足要求，满足的话记录窗口位置
            check = True
            for k, v in t_dic.items():
                if s_dic[k] < v:
                    check = False
            if check and r - l < res[1] - res[0]:
                res = [l, r]
        r += 1

    if res == [0, len(s)]:
        return ""
    return s[res[0]:res[1]+1]


if __name__ == "__main__":
    res = minWindow("ADOBECODEBANC", "ABC")
    print(res)