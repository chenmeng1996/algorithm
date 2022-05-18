

"""
https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/
"""
def minRemoveToMakeValid(s: str) -> str:
    """
    栈。

    栈只存储左括号和右括号的下标。
    在右括号入栈时, 寻找匹配的左括号, 如果找到了, 则出栈。
    最终栈保存的是不合法的括号下标, 删除这些下标即可。
    """
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                if s[stack[-1]] == ")":
                    stack.append(i)
                if s[stack[-1]] == "(":
                    stack.pop()
            else:
                stack.append(i)

    
    remove_set = set()
    for v in stack:
        if s[v] in ["(", ")"]:
            remove_set.add(v)
    res = []
    for i in range(len(s)):
        if i not in remove_set:
            res.append(s[i])
    return "".join(res)


if __name__ == "__main__":
    res = minRemoveToMakeValid("))((")
    print(res)