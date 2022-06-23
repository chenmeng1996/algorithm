"""
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""
def translateNum(num: int) -> int:
    def helper(num_str, start, res):
        if start > len(num_str) - 1:
            res[0] += 1
            return
        for i in range(1,3):
            if start+i-1 > len(num_str)-1:
                continue
            if i == 2 and num_str[start] == "0":
                continue
            if int(num_str[start:start+i]) > 25:
                continue
            helper(num_str, start+i, res)
    res = [0]
    helper(str(num), 0, res)
    return res[0]