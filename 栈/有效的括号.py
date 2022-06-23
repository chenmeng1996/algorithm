
"""
https://leetcode-cn.com/problems/valid-parentheses/
"""
def isValid(s: str) -> bool:
    """
    栈。
    从左往右遍历，往栈中加入括号。
    如果加入的是右括号，则查看是否可以与栈顶元素组成一对，可以组成一对则都弹出，否则入栈。
    """
    m = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3}
    stack = []
    for v in s:
        if len(stack) != 0 and m[v] < 0 and m[v] + stack[-1] == 0:
            stack.pop()
        else:
            stack.append(m[v])
    return len(stack) == 0
