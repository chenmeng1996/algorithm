"""
https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""

def reverseWords(s: str) -> str:
    """
    第一种方法：使用api进行split并reverse。
    第二种方法，双指针查找单词。
    """
    s = s.strip()
    i = j = len(s)-1
    res = []
    while i >= 0:
        while i >= 0:
            if s[i] != " ":
                i -= 1
            else:
                break
        res.append(s[i+1:j+1])
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break
        j = i
    return " ".join(res)


if __name__ == "__main__":
    res = reverseWords("the sky is blue")
    print(res)