import copy
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sort(values):
    """
    1. 遍历待排序数组，构造二叉排序树
    2. 中序遍历
    """
    root = None
    for v in values:
        root = add(root, v)
    values.clear()
    traverse(values, root)


def traverse(values, node: TreeNode):
    """
    中序遍历
    """
    if node:
        traverse(values, node.left)
        values.append(node.value)
        traverse(values, node.right)
    return values


def add(root: TreeNode, value):
    """
    构造二叉排序树
    """
    if not root:
        root = TreeNode(value)
        return root
    if value < root.value:
        root.left = add(root.left, value)
    else:
        root.right = add(root.right, value)
    return root


if __name__ == '__main__':
    vs = [3, 1, 7, 4, 5, 6]
    vs1 = vs
    sort(vs1)
    print(vs, vs1)