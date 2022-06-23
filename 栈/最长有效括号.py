
"""
https://leetcode.cn/problems/longest-valid-parentheses/

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""


def longestValidParentheses(s: str) -> int:
    """
    栈。
    栈存储下标。
    遇到匹配的左括号和右括号, 出栈, 并根据下标计算子串长度。
    """
    stack = []
    res = 0
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            stack.append(i)
        else:
            # 寻找匹配的左括号
            if stack and s[stack[-1]] == "(":
                stack.pop()
                # 有效括号的右边界是当前右括号
                right = i
                # 寻找左边界
                # 如果栈不为空, 则左边界是栈顶+1
                if stack:
                    left = stack[-1] + 1
                # 若果栈为空, 则左边界是数组第一个元素
                else:
                    left = 0
                length = right - left + 1
                res = max(res, length)
            else:
                stack.append(i)
    return res

if __name__ == "__main__":
    res = longestValidParentheses(")()())")
    print(res)



def longestValidParentheses1(s: str) -> int:
    """
    从左往右，记录左括号数量和右括号数量。
    1. 当左括号数量 < 右括号数量，不合法，重置计数器。
    2. 当左括号数量 = 右括号数量，合法，记录此时括号长度。
    3. 当左括号数量 > 右括号数量，可能合法，右边继续推进。（如果最终左括号数量大于右括号数量，会丢失一些case）。

    再从右往左，记录左括号数量和右括号数量。
    1. 当左括号数量 > 右括号数量，不合法，重置计数器。
    2. 当左括号数量 = 右括号数量，合法，记录此时括号长度。
    3. 当左括号数量 < 右括号数量，可能合法，左边继续推进
    """
    pass


def longestValidParentheses2(s: str) -> int:
    """
    动态规划。

    dp[i]表示以i结尾的最长有效括号长度。
    1. s[i-1] = "(", s[i] = ")", dp[i] = dp[i-2]+2
    2. s[i-1] = ")", s[i] = ")", dp[i] = 
    """
    pass

