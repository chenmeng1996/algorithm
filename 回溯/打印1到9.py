
import heapq


base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def printN(n):
    """
    全排列
    """
    res = []
    current = []
    def helper():
        if len(current) == n:
            s = "".join(current)
            i = 0
            while i < len(s):
                if s[i] != "0":
                    break
                i += 1
            if i == len(s):
                return
            if i != 0:
                s = s[i:]
            res.append(s)
            return
        for c in base:
            current.append(c)
            helper()
            current.pop()
    
    helper()
    print(res)

if __name__ == "__main__":
    print(printN(3))