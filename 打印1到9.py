base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def printN(n):
    """
    打印1到9*10的(n-1)次方的字符串。
    例如n=1，打印1,2,3...9
    例如n=2，打印1,2,3...9,10,11..99 (1-9) + []
    例如n=3，打印1,2,3...9,10,11..99,100,101..999 (1-9) + []
    例如n=4，打印1,2,3...9,10,11..99,100,101..999,1000,1001..9999 (1-9) + []
    f(n) = f(n-1) + [1-9]f(n-1)
    """
    if n == 1:
        return base
    res = []
    next_res = printN(n-1)
    for item in next_res:
        res.append(item)
    for i in range(1, 10):
        for item in next_res:
            if len(item) < n - 1:
                diff = n - 1 - len(item)
                s = str(i) + "0"*diff
            else:
                s = str(i)
            res.append(s+item)
    return res

if __name__ == "__main__":
    print(printN(4))