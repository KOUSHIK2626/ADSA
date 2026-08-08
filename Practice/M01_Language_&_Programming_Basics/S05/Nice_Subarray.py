'''
Nice subarray:
1248. Count Number of Nice Subarrays
1763. Longest Nice Substring
'''
#1248. Count Number of Nice Subarrays
from typing import List
def numberOfSubarrays(nums: List[int], k: int) -> int:
    def sub_arr(k):
        if k < 0:
            return 0
        left,odd,count = 0,0,0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
            while odd > k:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
            count += (right - left + 1)
        return count
    return sub_arr(k) - sub_arr(k-1)
nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums,k))

# 1763. Longest Nice Substring
def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""
    uniq = set(s)
    for i,ch in enumerate(s):
        if ch.lower() in uniq and ch.upper() in uniq:
            continue
        left_str = longestNiceSubstring(s[:i])
        right_str = longestNiceSubstring(s[i+1:])

        return left_str if len(left_str) >= len(right_str) else right_str
    return s
s1 = "YazaAay"
s2 = "Bb"
s3 = "c"
print(longestNiceSubstring(s1))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))