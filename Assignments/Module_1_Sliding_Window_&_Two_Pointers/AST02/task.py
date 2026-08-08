def Check_Palindrome(n: int, s: str) -> bool:
    left = 0
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            # Try deleting either the left or right character
            return s[left + 1:right + 1] == s[left + 1:right + 1][::-1] or \
                   s[left:right] == s[left:right][::-1]

        left += 1
        right -= 1

    return True
if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))