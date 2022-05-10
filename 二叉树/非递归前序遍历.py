from typing import List
from 二叉树 import TreeNode, build_tree1
from queue import Queue


def _push_left_to_stack(stack: list, root: TreeNode, visited):
    while root is not None:
        res.append(root)
        visited = root
        stack.append(root)
        root = root.left

def traverse(root: TreeNode):
    stack = []
    visited = None
    res = []
    _push_left_to_stack(stack, root, visited)
    while len(stack) != 0:
        top = stack[-1]
        # 左子树被访问过且右子树没被访问
        if top.left is None or (top.left == visited and top.right != visited):
            _push_left_to_stack(stack, top.right, visited)
        # 右子树访问过
        if top.right is None or top.right == visited:
            res.append(top)
            visited = stack.pop()



def traverse2(root: TreeNode) -> List[TreeNode]:
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
    res = traverse2(root)
    for node in res:
        print(node.value)