
from typing import List

class Trie:
    def __init__(self) -> None:
        self.next = {}
        self.is_leaf = False
    
    def add(self, s):
        t = self.next
        s_arr = s.split("/")[1:]
        for i in range(len(s_arr)):
            c = s_arr[i]
            if c not in t:
                t[c] = Trie()
            if i == len(s_arr)-1:
                t[c].is_leaf = True
            t = t[c].next
            
    
    def find(self, s):
        t = self.next
        s_arr = s.split("/")[1:]
        for i in range(len(s_arr)):
            c = s_arr[i]
            if c in t:
                if t[c].is_leaf and i < len(s_arr)-1:
                    return False
                t = t[c].next
        return True
                    
                

"""
https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/
"""
def removeSubfolders(folder: List[str]) -> List[str]:
    """
    字典树
    """
    trie = Trie()
    for f in folder:
        trie.add(f)
    
    res = []
    for f in folder:
        if trie.find(f):
            res.append(f)
    return res

def removeSubfolders2(folder: List[str]) -> List[str]:
    """
    排序，查看前缀
    """
    folder.sort()
    res = []
    for i in range(len(folder)):
        if i > 0 and folder[i].startswith(res[-1] + '/'):
            continue
        res.append(folder[i])
    return res

if __name__ == "__main__":
    res = removeSubfolders(["/ah/al/am","/ah/al"])
    print(res)