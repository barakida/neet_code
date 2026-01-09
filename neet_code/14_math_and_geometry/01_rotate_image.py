"""
Rotate Image

def rotate(matrix: List[List[int]]) -> None:

Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.
You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [
  [1,2],
  [3,4]
]
Output: [
  [3,1],
  [4,2]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List

EXAMPLES = [
    {"input": {"matrix": [[1,2], [3,4]]}, "output": [[3,1], [4,2]]},
    {"input": {"matrix": [[1,2,3], [4,5,6], [7,8,9]]}, "output": [[7,4,1], [8,5,2], [9,6,3]]}
]


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for c in range(n // 2):
        for i in range(c, n - 1 - c, 1):
            temp = matrix[c][i]
            matrix[c][i] = matrix[n - 1 - i][c]
            matrix[n - 1 - i][c] = matrix[n - 1 - c][n - 1 - i]
            matrix[n - 1 - c][n - 1 - i] = matrix[i][n - 1 - c]
            matrix[i][n - 1 - c] = temp


def main():
    for e in EXAMPLES:
        print(f"Input matrix: {e['input']['matrix']}")
        print(f"Expected Output matrix: {e['output']}")
        rotate(e['input']['matrix'])
        print(f"Output matrix: {e['input']['matrix']}\n\n")


if __name__ == '__main__':
    main()
