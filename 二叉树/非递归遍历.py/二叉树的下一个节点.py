

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

"""
https://mp.weixin.qq.com/s/yewlHvHSilMsrUMFIO8WAA
https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e

二叉树的节点有父亲节点的指针。
给定一个二叉树节点, 求该节点在中序遍历的下一个节点.
"""
def GetNext(pNode):
    """
    分情况讨论
    1. 节点有右孩子。则下一个节点是从右孩子一直往左遍历的节点。
    2. 节点没有右孩子, 分情况。
        2.1 节点是父节点的左孩子。则下一个节点是父节点。
        2.2 节点是父节点的右孩子。则沿着父节点一直向上寻找, 直到节点x是父节点的左孩子, 则下一个节点是节点x。
    """
    if pNode.right is not None:
        target = pNode.right
        while target.left is not None:
            target = target.left
        return target
    
    # root节点
    if pNode.next is None:
        return None

    if pNode.next.left == pNode:
        return pNode.next
    else:
        target = pNode.next
        while target.next is not None:
            if target.next.left == target:
                return target.next
            else:
                target = target.next
        return None
