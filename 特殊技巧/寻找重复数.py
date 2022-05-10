from typing import List


"""
https://leetcode-cn.com/problems/find-the-duplicate-number/
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

如果可以修改数组的话，可以使用原地哈希的方法，或者将数组元素为值的下标取反。
这两个方法都是遍历元素，将元素的值 与 索引（等于元素值）关联起来，从而在时间O(n)，空间O(1)的复杂度下解决问题。

如果不可以修改数组，方法是寻找链表环的入口。可以像遍历链表一样遍历数组。不同之处在于，链表通过next指针进入下一个节点，而数组使用value值作为下标，进入下一个节点。
因为数组有重复元素，所以这两个重复元素的next都是同一个节点。所以这就形成了链表环。
所以要先找到链表环的入口节点，然后next指向该入口节点的元素是重复元素。所以入口节点的元素值作为下标，就是重复元素。
"""
def findDuplicate(nums: List[int]) -> int:
    slow = fast = 0
    # 找slow和fast交界处
    while True:
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        if slow == fast:
            break
    # head和slow同时出发，最终会相等
    head = 0
    while head != slow:
        head = nums[head]
        slow = nums[slow]
    return slow


if __name__ == '__main__':
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([1,3,2,2]))