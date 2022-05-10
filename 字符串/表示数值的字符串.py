
def isNumber(s: str) -> bool:
    def check1(s):
        """是否是小数或整数"""
        dot_count = 0
        digit_count = 0
        for i in range(len(s)):
            if s[i] in ["+", "-"]:
                if i != 0:
                    return False
            elif s[i] == ".":
                dot_count += 1
                if dot_count > 1:
                    return False
            elif not s[i].isdigit():
                return False
            else:
                digit_count += 1
        if digit_count == 0:
            return False
        return True
    
    def check2(s):
        """是否是整数"""
        for i in range(len(s)):
            if s[i] in ["+", "-"]:
                if i != 0:
                    return False
            elif not s[i].isdigit():
                return False
            if i == len(s) - 1 and not s[i].isdigit():
                return False
        return True

    s = s.strip()
    s = s.lower()
    if s == "":
        return False
    l = s.split("e")
    if len(l) > 2:
        return False
    if len(l) == 1:
        pre = l[0]
        post = None
    else:
        pre = l[0]
        post = l[1]
        if len(pre) == 0:
            return False
        if len(post) == 0:
            return False
    if not check1(pre):
        return False
    if post is not None:
        return check2(post)
    else:
        return True

    
if __name__ == "__main__":
    res = isNumber("-1E-16")
    print(res)
    # s = "0e"
    # l = s.split("e")
    # print(l)