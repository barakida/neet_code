"""
Spiral Matrix

def spiral_order(matrix: List[List[int]]) -> List[int]:

Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [1,2,4,3]

Example 2:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 3:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

EXAMPLES = [
    {"input": {"matrix": [[1]]}, "output": [1]},
    {"input": {"matrix": [[1,2],[3,4]]}, "output": [1,2,4,3]},
    {"input": {"matrix": [[1,2,3],[4,5,6],[7,8,9]]}, "output": [1,2,3,6,9,8,7,4,5]},
    {"input": {"matrix": [[1,2,3,4],[5,6,7,8],[9,10,11,12]]}, "output": [1,2,3,4,8,12,11,10,9,5,6,7]},
]

def spiral_order(matrix: List[List[int]]) -> List[int]:
    results = []
    total = len(matrix[0]) * len(matrix)
    dy_dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, b, l, t = len(matrix[0]), len(matrix), -1, 0
    rblt_change = [(-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

    idx, iy, ix = 0, 0, 0
    dy, dx = dy_dx[idx]
    while len(results) < total:
        results.append(matrix[iy][ix])

        iy_, ix_ = iy + dy, ix + dx
        if not (l < ix_ < r or t < iy_ < b):
            dr, db, dl, dt = rblt_change[idx]
            r, b, l, t = r + dr, b + db, l + dl, t + dt
            idx = (idx + 1) % len(dy_dx)
            dy, dx = dy_dx[idx]
            iy_, ix_ = iy + dy, ix + dx
        iy, ix = iy_, ix_

    return results


function = spiral_order

def main():
    for e in EXAMPLES:
        print(f'input_matrix:\t{e["input"]["matrix"]}')
        print(f'expected_output:\t{e["output"]}')
        print(f'output_matrix:\t{function(**e["input"])}\n\n')


if __name__ == '__main__':
    main()