def palindrome(s: str):
    """
    寻找s的最长回文子串，思路是从中心向两边扩散寻找。
    回文子串的长度可能为奇数或偶数，为偶数时，会有两个中心点l和r。
    """
    m_length = 0
    res = []
    for l in range(len(s)):
        for i in range(2):
            left = l
            right = l + i
            if right < len(s) and s[left] != s[right]:
                continue
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            if (right - 1 - left) >= m_length:
                m_length = right - 1 - left
                res.append(s[left + 1:right])
    for v in res:
        if len(v) == m_length:
            print(v)

if __name__ == "__main__":
    palindrome("aba1233211")
