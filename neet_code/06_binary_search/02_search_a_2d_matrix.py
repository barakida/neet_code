"""
Search a 2D Matrix

def searchMatrix(matrix: List[List[int]], target: int) -> bool:

You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"matrix": [[1,2,4,8],[10,11,12,13],[14,20,30,40]], "target": 10}, "output": True},
    {"input": {"matrix": [[1,2,4,8],[10,11,12,13],[14,20,30,40]], "target": 15}, "output": False},
]

COMPLEXITY = """
O(log(m*n))
"""


def searchMatrix(matrix: List[List[int]], target: int) -> bool:

    # edge cases
    if not (matrix[0][0] <= target <= matrix[-1][-1]):
        return False

    # search for the right row
    r_min, r_max = 0, len(matrix) - 1
    while r_min <= r_max:
        r = (r_min + r_max) // 2
        if target < matrix[r][0]:
            r_max = r - 1
        elif matrix[r][-1] < target:
            r_min = r + 1
        else:
            break

    # edge cases
    if not (matrix[r][0] <= target <= matrix[r][-1]):
        return False

    # search for the right column
    c_min, c_max = 0, len(matrix[r]) - 1
    while c_min <= c_max:
        c = (c_min + c_max) // 2
        if target == matrix[r][c]:
            return True
        elif target < matrix[r][c]:
            c_max = c - 1
        elif matrix[r][c] < target:
            c_min = c + 1

    return False


function = searchMatrix


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
