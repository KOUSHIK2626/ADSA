'''
Longest substring based:
3. Longest Substring Without Repeating Characters
424. Longest Repeating Character Replacement
'''
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    s1 = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in s1:
            s1.remove(s[left])
            left += 1
        s1.add(s[right])
        max_len = max(max_len,right - left + 1)        
    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))