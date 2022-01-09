from typing import List
from tree import TreeNode, build_tree1

def traverse(root: TreeNode) -> List[TreeNode]:
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
    res = traverse(root)
    for node in res:
        print(node.value)