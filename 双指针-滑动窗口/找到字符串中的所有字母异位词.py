"""
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
"""

from collections import defaultdict
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    """
    1. 记录p的所有字符以及字符的出现次数
    2. 在s中用滑动窗口统计字符以及字符的出现次数。
    """
    target = defaultdict(int)
    for v in p:
        target[v] += 1
    current = defaultdict(int)
    res = []
    i = 0
    j = 0
    while j < len(s):
        current[s[j]] += 1
        if s[j] not in target:
            # 重置窗口
            j = j + 1
            i = j
            current.clear()
        elif current[s[j]] > target[s[j]]:
            # 左边窗口向右滑动，直到把多余的元素删掉，然后右边窗口移动一位
            while i <= j:
                if current[s[j]] <= target[s[j]]:
                    break
                current[s[i]] -= 1
                i += 1
            j += 1
        else:
            if current == target:
                # 找到目标窗口，记录并将窗口平移一位
                res.append(i)
                current[s[i]] -= 1
                i += 1
                j += 1
            else:
                # 还没找到窗口，但目前还符合预期，右边窗口继续滑动
                j += 1
    return res


if __name__ == "__main__":
    res = findAnagrams("abab", "ab")
    print(res)