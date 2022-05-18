

"""
https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/

如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 text, 你只能交换其中两个字符 一次 或者什么都不做，然后得到一些单字符重复的子串。
返回其中最长的子串的长度。
"""
def maxRepOpt1(text: str) -> int:
    """
    统计每个字符的出现次数。
    滑动窗口, 当遇到不一样的字符时, 判断补上可不可以延续。
    """
    counter = [0]*26
    for c in text:
        counter[ord(c) - ord("a")] += 1
    
    res = 0
    n = len(text)
    i = 0
    while i < n:
        length = 0
        while i + length < n and text[i+length] == text[i]:
            length += 1
        j = i + length + 1
        w = 0
        while j+w < n and text[j+w] == text[i]:
            w += 1
        res = max(res, min(w+length+1, counter[ord(text[i]) - ord("a")]))
        i += length
    return res


if __name__ == "__main__":
    text = "acbaaa"
    res = maxRepOpt1(text)
    print(res)