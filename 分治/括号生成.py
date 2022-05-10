from typing import List


def generateParenthesis(n: int) -> List[str]:
    """
    递归使用左括号和右括号，记录剩余的左括号数量和右括号数量。
    如果剩余的左括号和右括号相同，则必须使用左括号。
    如果剩余的左括号小于右括号，则使用左括号和右括号都可以，都需要试一下。
    """
    def helper(res, s, left, right):
        if right == 0:
            res.append(s)
            return
        if left == right:
            helper(res, s+"(", left-1, right)
        else:
            if left > 0:
                helper(res, s+"(", left-1, right)
            helper(res, s+")", left, right-1)
    res = []
    s = ""
    helper(res, s, n, n)
    return res


if __name__ == "__main__":
    res = generateParenthesis(3)
    print(res)