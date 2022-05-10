def lengthOfLongestSubstring(s: str) -> int:
    """
    滑动窗口 + set
    """
    max_count = 0
    visited = set()
    right = -1
    for i in range(len(s)):
        if i != 0:
            visited.remove(s[i-1])
        # 右指针向右移动
        while right+1 < len(s) and s[right+1] not in visited:
            visited.add(s[right+1])
            right += 1
        max_count = max(max_count, len(visited))
    return max_count
