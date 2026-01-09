"""
Set Matrix Zeroes

def set_zeroes(matrix: List[List[int]]) -> None:

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.
You must update the matrix in-place.
Follow up: Could you solve it using O(1) space?

Example 1:
Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]

Constraints:
1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1
"""
from typing import List

EXAMPLES = [
    {"input": {
        "matrix": [
          [0,1],
          [1,0]
        ]}, "output": [
          [0,0],
          [0,0]
        ]},
    {"input": {
        "matrix": [
          [1,2,3],
          [4,0,5],
          [6,7,8]
        ]}, "output": [
          [1,0,3],
          [0,0,0],
          [6,0,8]
        ]},
]

COMPLEXITY = """
Complexity:
time: O(n*m)
space: O(m + n)
"""

def set_zeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    for row in range(rows):
        for col in range(cols):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0


function = set_zeroes


def main():
    for e in EXAMPLES:
        print(f"Input: {e['input']}")
        print(f"Expected: {e['output']}")
        function(**e['input'])
        print(f"Input: {e['input']}\n\n")

    print(COMPLEXITY)

if __name__ == '__main__':
    main()


"""
GPT solution (using O(1) space)
he uses the first row a col as markers.

def set_zeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])

    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

    # mark zeros
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # zero marked rows and columns
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # zero first row if needed
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    # zero first column if needed
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
"""
