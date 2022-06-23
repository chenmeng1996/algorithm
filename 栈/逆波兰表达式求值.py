

from typing import List


"""
https://leetcode.cn/problems/evaluate-reverse-polish-notation/
"""
def evalRPN(tokens: List[str]) -> int:
    """
    栈。
    遇到操作符, 弹出栈顶两个元素, 计算后将值入栈。
    """
    def calc(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            # 负数用//有问题
            return int(a / b)
    
    def is_num(a: str):
        if a[0] == "-":
            return a[1:].isdigit()
        else:
            return a.isdigit()

    stack = []
    for v in tokens:
        if is_num(v):
            stack.append(int(v))
        else:
            b = stack.pop()
            a = stack.pop()
            res = calc(a, b, v)
            stack.append(res)
    return stack[0]


if __name__ == "__main__":
    res = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(res)