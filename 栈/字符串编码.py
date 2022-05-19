
"""
https://leetcode-cn.com/problems/decode-string/
"""
def decodeString(s: str) -> str:
    """
    栈。
    记录"[" 和 "]"。
    """
    stack = []
    for v in s:
        if v != "]":
            stack.append(v)
        else:
            l = []
            while stack:
                if stack[-1] == "[":
                    stack.pop()
                    break
                else:
                    l.append(stack.pop())
            l.reverse()
            nums = []
            while stack:
                if not stack[-1].isdigit():
                    break
                else:
                    nums.append(stack.pop())
            nums.reverse()
            num = int("".join(nums))
            for _ in range(int(num)):
                stack.extend(l)
    return "".join(stack)


if __name__ == "__main__":
    res = decodeString("3[a2[c]]")
    print(res)