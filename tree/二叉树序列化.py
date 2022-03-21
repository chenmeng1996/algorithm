# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            current = queue.get()
            if current is None:
                s.append("null")
                continue
            s.append(str(current.val))
            queue.put(current.left)
            queue.put(current.right)
        return ",".join(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(",")
        root = None
        flag = 0 # 下一次插入是左孩子还是右孩子
        queue = Queue() # 等待被插入左右孩子的节点
        last = None
        for c in l:
            if c == "null":
                next_node = None
            else:
                next_node = TreeNode(c)
            # 第一个节点的初始化
            if root is None:
                root = next_node
                queue.put(next_node)
            else:
                if next_node is not None:
                    queue.put(next_node)
                # 左
                if flag == 0:
                    last = queue.get()
                    last.left = next_node
                    flag = 1
                # 右
                else:
                    last.right = next_node
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
