from typing import List
from 二叉树 import TreeNode, build_tree1

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
            res.append(top)
            visited = stack.pop()
            _push_left_to_stack(stack, top.right)






def traverse2(root: TreeNode) -> List[TreeNode]:
    res = []
    stack = []
    current = root

    while current is not None or len(stack) != 0:
        while current is not None:
            # 对左孩子进行递归，保存路径
            stack.append(current)
            current = current.left
        # 左孩子递归结束后，打印最后一个节点，并对右孩子重复递归步骤
        last = stack.pop()
        res.append(last)
        current = last.right
    return res

if __name__ == "__main__":
    root = build_tree1()
    res = traverse2(root)
    for node in res:
        print(node.value)