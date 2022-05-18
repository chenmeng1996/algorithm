

from typing import List

"""
https://leetcode.cn/problems/making-file-names-unique/
"""
def getFolderNames(names: List[str]) -> List[str]:
    """
    哈希表记录每个文件名的后缀到哪个编号了。
    加后缀的文件名也应该保存到哈希表。
    """
    dic = {}
    res = []
    for name in names:
        if name in dic:
            k = dic[name]
            while True:
                k += 1
                new_name = name + "(" + str(k) + ")"
                if new_name not in dic:
                    dic[new_name] = 0
                    dic[name] += 1
                    res.append(new_name)
                    break
                else:
                    continue
        else:
            dic[name] = 0
            res.append(name)
    return res