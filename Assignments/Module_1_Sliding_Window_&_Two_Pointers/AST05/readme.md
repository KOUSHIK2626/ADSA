# Product of Array Except Self
Given an array arr[] of n integers, construct a product array res[] (of the same size) such that res[i] is equal to the product of all the elements of arr[] except arr[i]. 

### Example: 
```
Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: 
For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: 
For i = 0, res[i] = 0.
For i = 1, res[i] = 12.
```

## Instructions
1. Write your solution in `task.py`
2. Do NOT modify `test_task.py`
3. Run tests locally before pushing

## Submission Rules
- Only `task.py` will be evaluated
