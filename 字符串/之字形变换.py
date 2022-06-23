
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    l = [[] for _ in range(numRows)]
    i = 0
    step = 1
    for c in s:
        l[i].append(c)
        if i == 0:
            step = 1
        if i == numRows-1:
            step = -1
        i += step
    res = ""
    for v in l:
        res += "".join(v)
    return res


if __name__ == "__main__":
    res = convert("PAYPALISHIRING", 3)
    print(res)
