from typing import List

"""
https://leetcode.cn/problems/validate-stack-sequences/
https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
"""
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    """
    根据出栈元素, 模拟入栈操作。
    注意使用set来存储已经入栈的元素。
    """
    stack = []
    visited = set()
    # 记录入栈队列的访问位置
    index = 0
    for pop in popped:
        # 如果弹出元素已经在栈中, 就不需要再入栈了
        if pop not in visited:
            # 出栈元素之前的元素都入栈
            for i in range(index, len(pushed)):
                stack.append(pushed[i])
                visited.add(pushed[i])
                if pushed[i] == pop:
                    index = i + 1
                    break
        # 出栈
        x = stack.pop()
        if x != pop:
            return False
    return True