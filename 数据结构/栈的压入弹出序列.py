from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    visited = set()
    index = 0
    for pop in popped:
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