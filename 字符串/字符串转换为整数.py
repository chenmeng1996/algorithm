
def myAtoi(s: str) -> int:
    s = s.strip()
    negative = False
    if len(s) == 0:
        return 0
    if s[0] == "-":
        negative = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    for i in range(len(s)):
        if not s[i].isdigit():
            s = s[:i]
            break
    max_num = 2**31
    def check_bound(num):
        over = False
        if not negative:
            if num > max_num - 1:
                num = max_num - 1
                over = True
        else:
            if num > max_num:
                num = max_num
                over = True
        return num, over

    res = 0
    for i in range(len(s)):
        num = int(s[i])
        res = 10 * res
        res += num
        res, over = check_bound(res)
        if over:
            break
        else:
            res, over = check_bound(res)
            if over:
                break
    return -res if negative else res
        

if __name__ == "__main__":
    res = myAtoi("4193 with words")
    print(res)