from typing import List

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # Product of elements to the left
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Product of elements to the right
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))