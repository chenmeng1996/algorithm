from typing import List
from tree import TreeNode, build_tree1
from queue import Queue

def traverse(root: TreeNode) -> List[TreeNode]:
    '''队列记录下一个要处理的节点。
    栈记录处理过的节点'''
    q = Queue()
    q.put(root)
    stack = []
    while not q.empty():
        first = q.get()
        if first is None:
            continue
        stack.append(first)
        q.put(first.right)
        q.put(first.left)
    res = []
    while len(stack) != 0:
        res.append(stack.pop())
    return res
    
if __name__ == "__main__":
    root = build_tree1()
    res = traverse(root)
    for node in res:
        print(node.value)