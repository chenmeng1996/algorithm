
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
https://leetcode-cn.com/problems/copy-list-with-random-pointer/
"""
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    递归的拷贝next和random指向的指针。
    """
    def helper(head, copyed):
        if head is None:
            return None
        new_head = Node(head.val)
        copyed[head] = new_head
        if head.next not in copyed:
            new_head.next = helper(head.next, copyed)
        else:
            new_head.next = copyed[head.next]
        if head.random not in copyed:
            new_head.random = helper(head.random, copyed)
        else:
            new_head.random = copyed[head.random]
        return new_head
    
    return helper(head, {})