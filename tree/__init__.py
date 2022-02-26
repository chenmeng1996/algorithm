class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(values):
    root = TreeNode()
    nodes = []
    for i in range(len(values)):
        if i == 0:
            root.value = values[i]
            nodes.append(root)
            continue
        # 构造新节点
        new_node = TreeNode(value=values[i]) if values[i] is not None else None
        nodes.append(new_node)
        # 新节点的父节点索引
        parent_index = (i - 1) // 2
        if i % 2 != 0:
            nodes[parent_index].left = new_node
        else:
            nodes[parent_index].right = new_node
    return root

def print_tree(root: TreeNode):
    def __print_tree(root: TreeNode):
        if root is None:
            return
        print(root.value)
        __print_tree(root.left)
        __print_tree(root.right)
    __print_tree(root)

def build_tree1() -> TreeNode:
    return build_tree([1, 2, 3, 4, None, None, None, None, None])