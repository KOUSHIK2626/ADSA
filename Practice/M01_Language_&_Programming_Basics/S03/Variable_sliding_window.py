'''
Variable sliding window Problems:
Array based:
209. Minimum Size Subarray Sum
713. Subarray product less than K
904. Fruit Into Baskets
'''
from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    left,curr_sum = 0,0
    min_len = float("inf")
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len,right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    left,count = 0,0
    p = 1
    for right in range(len(nums)):
        p *= nums[right]
        while p >= k:
            p //= nums[left] 
            left += 1
        count += (right - left + 1)
    return count  
nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))