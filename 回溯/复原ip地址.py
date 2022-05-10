
from typing import List


"""
https://leetcode-cn.com/problems/restore-ip-addresses/
"""
def restoreIpAddresses(s: str) -> List[str]:
    """
    回溯。
    最多四次递归，且每个字符串满足以下条件：
    1. s长度不能超过3位。
    2. s长度如果超过1位，不能以0开头。
    3. int(s) <= 255
    """
    def helper(s, start, depth, res, cur):
        for end in range(start, len(s)):
            if end - start > 2:
                break
            if end - start > 0 and s[start] == "0":
                break
            if int(s[start:end+1]) > 255:
                break
            cur.append(s[start:end+1])
            if depth == 4 and end == len(s) - 1:
                res.append(".".join(cur))
            if depth < 4:
                helper(s, end+1, depth+1, res, cur)
            cur.pop()
    
    res = []
    cur = []
    helper(s, 0, 1, res, cur)
    return res
