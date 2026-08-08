'''
input : [12,45,63,20,96,25,10]
output : [12,20,96,10]

Brute-force approach:

arr = list(map(int,input().split()))
res = []
for ele in arr:
    if ele % 2 == 0:
        res.append(ele)
print(res)

arr = list(map(int,input().split()))
i = 0
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1
print(arr[:i])

s = input()
li = list(s)
left,right = 0,len(s)-1
while left < right:
    li[left],li[right] = li[right],li[left]
    left += 1
    right -= 1
print("".join(li))
'''

'''
input : [12,45,36,89,75,63,20]
output : [12,36,20]

arr = list(map(int,input().split()))
res = []
for ele in arr:
    if ele % 2 == 0:
        res.append(ele)
print(res)
'''
arr = list(map(int,input().split()))
i = 0
for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1
print(arr[:i])