'''
1480 – Running Sum of 1d Array
303 – Range Sum Query - Immutable
724 – Find Pivot Index
1991 – Find the Middle Index in Array
1732 – Find the Highest Altitude
560 – Subarray Sum Equals K
'''
'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
'''
#Brute-force
nums = [1,2,3,4]
n = len(nums)
res = [0] * n 
for i in range(n):
    s = 0
    for j in range(0,i+1):
        s += nums[j]
    res[i] = s
print(res)

#Optimal solution
nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i] + nums[i-1]
print(nums)

from typing import List
def largestAltitude(gain: List[int]) -> int:
    '''
    n = len(gain)
    alt = [0] * (n+1)
    for i in range(1,n+1):
        alt[i] = alt[i-1] + gain[i-1]
    return max(alt)
    '''
    curr_alt = 0
    max_alt = 0
    for g in gain:
        curr_alt += g
        max_alt = max(max_alt,curr_alt)
    return max_alt
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

def runningSum(nums: List[int]) -> List[int]:
    res = []
    s = 0
    for ele in nums:
        s += ele
        res.append(s)
    return res
nums = [1,2,3,4]
print(runningSum(nums))
