from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



"""
https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/
"""
class Codec:

    def serialize(self, root):
        """
        不区分层的层次遍历.
        """
        s = []
        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            if current is None:
                s.append("null")
                continue
            s.append(str(current.val))
            queue.append(current.left)
            queue.append(current.right)
        return ",".join(s)
        

    def deserialize(self, data):
        """
        根据层次遍历，构造二叉树。
        使用队列存储。队头元素是需要插入孩子的元素（需要记录要插入左孩子还是右孩子）。
        当左孩子和右孩子都插入完毕，将队头元素删除。
        """
        l = data.split(",")
        root = None
        flag = 0 # 队头元素下一次插入是左孩子还是右孩子
        queue = deque() # 等待被插入左右孩子的节点
        for c in l:
            # 构造节点
            if c == "null":
                next_node = None
            else:
                next_node = TreeNode(c)
            # 根节点的初始化
            if root is None:
                root = next_node
                # 加入队列，后面要插入左右孩子
                queue.append(next_node)
            else:
                # 新节点加入队列，后面要插入左右孩子
                if next_node is not None:
                    queue.append(next_node)
                # 新节点作为队头元素的左孩子
                if flag == 0:
                    father = queue[0]
                    father.left = next_node
                    flag = 1
                # 新节点作为队头元素的右孩子，队头元素左右孩子都插入了，出队列。
                else:
                    father = queue.popleft()
                    father.right = next_node
                    flag = 0
        return root
                
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def build_tree(values):
    root = TreeNode(None)
    nodes = []
    for i in range(len(values)):
        if i == 0:
            root.val = values[i]
            nodes.append(root)
            continue
        # 构造新节点
        new_node = TreeNode(values[i]) if values[i] is not None else None
        nodes.append(new_node)
        # 新节点的父节点索引
        parent_index = (i - 1) // 2
        if i % 2 != 0:
            nodes[parent_index].left = new_node
        else:
            nodes[parent_index].right = new_node
    return root


if __name__ == "__main__":
    root = build_tree([1,2,3,None,None,4,5])
    codec = Codec()
    s = codec.serialize(root)
    print(s)

    t = codec.deserialize(s)
    s = codec.serialize(t)
    print(s)
