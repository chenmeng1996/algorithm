
"""
https://leetcode.cn/problems/additive-number/

累加数 是一个字符串，组成它的数字可以形成累加序列。
"""
def isAdditiveNumber(self, num: str) -> bool:
    def dfs(num, firstnum, secondnum):
        if not num: 
            return True
        total = firstnum + secondnum
        length = len(str(total))
        if str(total) == num[:length]:
            return dfs(num[length:], secondnum, total)
        return False

    for i in range(1, len(num)-1):
        if num[0] == '0' and i > 1:
            break
        for j in range(i+1, len(num)):
            if j-i > 1 and num[i] == '0':
                break
            if dfs(num[j:], int(num[:i]), int(num[i:j])): 
                return True
    return False