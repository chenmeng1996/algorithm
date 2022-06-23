

"""
https://leetcode.cn/problems/basic-calculator-ii/

计算表达式只包含非负整数、+、-、*、/
"""
def calculate(s: str) -> int:
    """
    双栈, 分别存储数字和操作符
    """
    nums_stack = []
    opt_stack = []
    s = s.replace(" ", "")
    n = len(s)
    # 操作符优先级
    m = {"-": 1, "+": 1, "*": 2, "/": 2}

    def calc(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a // b
        return 0

    i = 0
    while i < n:
        c = s[i]
        if c.isdigit():
            # 搜索一个整数
            j = i
            while j < n and s[j].isdigit():
                j += 1
            nums_stack.append(int(s[i:j]))
            i = j - 1
        else:
            # 新操作符入栈时，先将栈内优先级相同或更高的操作计算。
            while opt_stack:
                if m[opt_stack[-1]] >= m[c]:
                    op = opt_stack.pop()
                    b = nums_stack.pop()
                    a = nums_stack.pop()
                    res = calc(a, b, op)
                    nums_stack.append(res)
                else:
                    break
            opt_stack.append(c)
        i += 1
    
    # 最后一个操作符计算
    while opt_stack:
        op = opt_stack.pop()
        b = nums_stack.pop()
        a = nums_stack.pop()
        res = calc(a, b, op)
        nums_stack.append(res)
    
    return nums_stack[0]



if __name__ == "__main__":
    res = calculate("0-2147483647")
    print(res)