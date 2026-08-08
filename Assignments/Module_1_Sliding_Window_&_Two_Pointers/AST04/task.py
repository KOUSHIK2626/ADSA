def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    # Find the pivot (index of the largest element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break

    # If the array is not rotated
    if pivot == 0 and arr[0] <= arr[-1]:
        pivot = n - 1

    left = (pivot + 1) % n       # smallest element
    right = pivot                 # largest element

    while left != right:
        total = arr[left] + arr[right]

        if total == target:
            return True

        if total < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))