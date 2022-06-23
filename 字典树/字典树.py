class Trie:
    """
    前缀树，或者叫字典树，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

    构造内部节点，节点组成：哈希表、是否是单词。哈希表的key是单词的字符，value是节点。
    """

    class TreeNode:
        def __init__(self) -> None:
            self.nexts = {}
            self.is_leaf = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = Trie.TreeNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.tree
        for c in word:
            if c in current_node.nexts:
                next_node = current_node.nexts[c]
            else:
                next_node = Trie.TreeNode()
                current_node.nexts[c] = next_node
            current_node = next_node
        current_node.is_leaf = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.tree
        for c in word:
            if c not in current_node.nexts:
                return False
            current_node = current_node.nexts[c]
        return current_node.is_leaf


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.tree
        for c in prefix:
            if c not in current_node.nexts:
                return False
            current_node = current_node.nexts[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # 返回 True
    print(trie.search("app"))    # 返回 False
    print(trie.startsWith("app")) # 返回 True
    trie.insert("app") 
    print(trie.search("app"))  # 返回 True