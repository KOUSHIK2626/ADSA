'''
54. Spiral Matrix 
59. Spiral Matrix II 
'''
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows,cols = len(matrix),len(matrix[0])
    top,bottom = 0,rows - 1
    left,right = 0,cols - 1
    res = []
    while top <= bottom and left <= right:
        #left -> right
        for col in range(left,right+1):
            res.append(matrix[top][col])
        top += 1

        #top to bottom
        for row in range(top,bottom+1):
            res.append(matrix[row][right])
        right -= 1

        #right to left
        if top <= bottom:
            for col in range(right,left-1,-1):
                res.append(matrix[bottom][col])
            bottom -= 1

        #bottom to top
        if left <= right:
            for row in range(bottom,top-1,-1):
                res.append(matrix[row][left])
            left += 1
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

def generateMatrix(n: int) -> List[List[int]]:
    top,bottom = 0,n - 1
    left,right = 0,n - 1
    num = 1
    res = [[0]*n for _ in range(n)]
    while top <= bottom and left <= right:
        #left -> right
        for col in range(left,right+1):
            res[top][col] = num
            num += 1
        top += 1

        #top to bottom
        for row in range(top,bottom+1):
            res[row][right] = num
            num += 1
        right -= 1

        #right to left
        if top <= bottom:
            for col in range(right,left-1,-1):
                res[bottom][col] = num
                num += 1
            bottom -= 1

        #bottom to top
        if left <= right:
            for row in range(bottom,top-1,-1):
                res[row][left] = num
                num += 1
            left += 1
    return res
n = 3
print(generateMatrix(n))
