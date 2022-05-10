"""
给定一个字符串文本（有很多字符串）和一个字符串数组（字符串也很多），查询字符串文本中每个字符串在字符串数组中的下标位置。
"""

"""
将字符串数组构建成一个字典树。遍历字符串文本的每个字符串，在字典树中查找。
"""
class Trie:
    def __init__(self) -> None:
        self.nexts = {}
        self.is_leaf = False
        self.index = 0
    

    def insert(self, s, index):
        target = self
        for i in range(len(s)):
            v = s[i]
            if v in target.nexts:
                target = target.nexts[v]
            else:
                target.nexts[v] = Trie()
                target = target.nexts[v]
            # 到末尾了，写入数据
            if i == len(s)-1:
                target.index = index
                target.is_leaf = True
    

    def search(self, s) -> int:
        target = self
        for i in range(len(s)):
            v = s[i]
            if v in target.nexts:
                target = target.nexts[v]
                if i == len(s)-1:
                    if target.is_leaf:
                        return target.index
                    else:
                        return -1
            else:
                return -1


if __name__ == "__main__":
    to_be_searched = "abc"
    target = ["ab", "de", "acb", "abcd", "abc"]
    trie = Trie()
    for i in range(len(target)):
        trie.insert(target[i], i)
    print(trie.search(to_be_searched))