from typing import List
from tree import TreeNode, build_tree1
from queue import Queue


def _push_left_to_stack(stack: list, root: TreeNode):
    while root is not None:
        stack.append(root)
        root = root.left

def traverse(root: TreeNode):
    stack = []
    visited = None
    res = []
    _push_left_to_stack(stack, root)
    while len(stack) != 0:
        top = stack[-1]
        # 左子树被访问过且右子树没被访问
        if top.left is None or (top.left == visited and top.right != visited):
            _push_left_to_stack(stack, top.right)
        # 右子树访问过
        if top.right is None or top.right == visited:
            res.append(top)
            visited = stack.pop()


def traverse2(root: TreeNode) -> List[TreeNode]:
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
    res = traverse2(root)
    for node in res:
        print(node.value)