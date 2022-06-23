

# Definition for a Node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    """
    非递归，利用队列实现二叉树层次遍历
    """
    if root is None:
        return None
    que = deque() # 存储一层的节点
    que.append(root)
    while len(que) != 0:
        # 当层节点从左到右连接
        for i in range(len(que)-1):
            que[i].next = que[i+1]
        # 清空当层节点，添加下一层节点
        for _ in range(len(que)):
            x = que.popleft()
            if x.left is not None:
                que.append(x.left)
            if x.right is not None:
                que.append(x.right)
    return root



def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    """
    递归
    """
    def connect_two_node(node1: Node, node2: Node):
        """将相临节点连接"""
        if node1 is None or node2 is None:
            return
        node1.next = node2
        # 节点1的左孩子和右孩子，节点2的左孩子和右孩子， 节点的1的右孩子和节点2的左孩子
        connect_two_node(node1.left, node1.right)
        connect_two_node(node2.left, node2.right)
        connect_two_node(node1.right, node2.left)
    
    if root is None:
        return None
    connect_two_node(root.left, root.right)
    return root
        