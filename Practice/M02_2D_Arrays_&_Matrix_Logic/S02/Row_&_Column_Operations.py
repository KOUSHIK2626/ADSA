'''
1351 - Count Negative Numbers in a Sorted Matrix 
832 – Flipping an Image
'''
#1351 - Count Negative Numbers in a Sorted Matrix 
from typing import List
def countNegatives_brute(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        for ele in row:
            if ele < 0:
                count += 1
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_brute(grid))

#Optimal solution using sorted row
def countNegatives_optimal(grid: List[List[int]]) -> int:
    rows,cols = len(grid),len(grid[0])
    count = 0
    for r in range(rows):
        for c  in range(cols):
            if grid[r][c] < 0:
                count += (cols - c)
                break
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_optimal(grid))

#832 – Flipping an Image
def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        row.reverse()
        for j in range(len(row)):
            #row[j] = 1 if row[j] == 0 else 0
            row[j] = 1 - row[j]
    return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))