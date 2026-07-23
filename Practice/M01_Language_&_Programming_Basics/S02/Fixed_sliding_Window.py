# Brute force approach to find the maximum average of a subarray of length k
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_avg = float("-inf")
    n = len(nums)
    for i in range(0, n - k + 1):
        sub_sum = 0
        for j in range(i, k + i):
            sub_sum += nums[j]
        max_avg = max(max_avg, sub_sum / k)
    return max_avg
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))



def findMaxAverage_Optimal(nums: List[int], k: int) -> float:
    n = len(nums)
    win_sum = sum(nums[0:k])
    for i in range(n-k):
        next_win_sum = win_sum - nums[i] + nums[k+i]
        win_sum = max(win_sum, next_win_sum)
    return win_sum / k
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage_Optimal(nums, k))