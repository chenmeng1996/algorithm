
def connect(root: TreeNode) -> TreeNode:
    """
    递归
    """
    if root is None:
        return None
    connect_two_node(root.left, root.right)
    return root


def connect_two_node(node1: TreeNode, node2: TreeNode):
    """
    将相临节点连接
    """
    if node1 is None or node2 is None:
        return
    node1.next = node2
    connect_two_node(node1.left, node1.right)
    connect_two_node(node2.left, node2.right)
    connect_two_node(node1.right, node2.left)


def connect2(root: TreeNode) -> TreeNode:
    """
    非递归，利用队列实现二叉树层次遍历
    """
    queue = [] # 存储一层的节点
    cur = root
    queue.append(cur)
    while len(queue) != 0:
        # 当层节点从左到右连接
        for i in range(len(queue)-1):
            queue[i].next = queue[i+1]
        # 清空当层节点，添加下一层节点
        for v in queue:
            if cur.left is not None:
                queue.append(v.left)
            if cur.right is not None:
                queue.append(v.right)
            queue.pop(v)
    return root
        