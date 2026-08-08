'''
Binary subarray
1493. Longest Subarray of 1's After Deleting One Element
1004. Max Consecutive Ones III 
930. Binary Subarrays With Sum  
'''
from typing import List
#1493. Longest Subarray of 1's After Deleting One Element
def longestSubarray(nums: List[int]) -> int:
    left = 0
    max_len = 0
    zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len,right - left + 1)
    return max_len - 1
nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))

#1004. Max Consecutive Ones III
def longestOnes(nums: List[int], k: int) -> int:
    left,max_len = 0,0
    zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len,right-left+1)
    return max_len
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))