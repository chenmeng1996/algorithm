from typing import List


def generateParenthesis(n: int) -> List[str]:
    """
    当前的括号是否有效: 左括号数量 >= 右括号数量

    回溯法, 生成所有括号。
    每次加括号, 有两种选择, 加左括号或者右括号
    """
    def helper(res, s, left, right):
        if right == 0:
            res.append("".join(cur))
            return
        if left == right:
            cur.append("(")
            helper(res, cur, left-1, right)
            cur.pop()
        else:
            if left > 0:
                cur.append("(")
                helper(res, cur, left-1, right)
                cur.pop()
            cur.append(")")
            helper(res, cur, left, right-1)
            cur.pop()
    res = []
    cur = []
    helper(res, cur, n, n)
    return res


if __name__ == "__main__":
    res = generateParenthesis(3)
    print(res)