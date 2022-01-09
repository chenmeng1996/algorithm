from typing import List
from tree import TreeNode, build_tree1
from queue import Queue

def traverse(root: TreeNode) -> List[TreeNode]:
    res = []
    q = Queue()
    q.put(root)
    while not q.empty():
        first = q.get()
        if first is None:
            continue
        res.append(first)
        q.put(first.left)
        q.put(first.right)
    return res
    
if __name__ == "__main__":
    root = build_tree1()
    res = traverse(root)
    for node in res:
        print(node.value)