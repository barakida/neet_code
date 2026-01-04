"""
Surrounded Regions

def solve(board: List[List[str]]) -> None:

You are given a 2-D matrix board containing 'X' and 'O' characters.
If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.
Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
"""

EXAMPLES = [
    {"input": {"board": [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","O"]
    ]},
    "output": [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","O"]
    ]},
]

COMPLEXITY = """
Complexity
Let R = rows, C = cols.
Each cell is processed at most once in BFS and once in the final scan.
Time: O(R⋅C)
Space: O(R⋅C)
Queue can hold up to R·C cells in worst case.
(And it’s in-place except for the queue.)
"""

from collections import deque
from typing import List


def solve(board: List[List[str]]) -> None:

    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def save_cell(r_: int, c_: int) -> None:
        if board[r_][c_] == "O":
            board[r_][c_] = "S"
            queue.append((r_, c_))

    queue = deque()
    for r in range(rows):
        save_cell(r, 0)
        save_cell(r, cols - 1)
    for c in range(1, cols - 1, 1):
        save_cell(0, c)
        save_cell(rows - 1, c)

    while queue:
        r, c = queue.popleft()
        for (y, x) in directions:
            nr, nc = r + y, c + x
            if 0 <= nr < rows and 0 <= nc < cols:
                save_cell(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"


function = solve


if __name__ == '__main__':
    import numpy as np

    for e in EXAMPLES:
        print(f"{np.array(e['input']["board"])}")
        print(function(**e['input']))
        print()
        print(f"{np.array(e['input']["board"])}")
        print("\n\n")

    print("\nComplexity:", COMPLEXITY)


"""

"""