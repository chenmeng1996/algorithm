

from collections import defaultdict
from typing import List

"""
https://leetcode.cn/problems/group-anagrams/
"""
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    统计每个单词的每个字母的出现次数, 将这个结果作为key。
    通过哈希表存储相同key的单词, 即可分组。
    """
    res = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())


if __name__ == "__main__":
    res = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)