"""
Valid Sudoku

def isValidSudoku(board: List[List[str]]) -> bool:

You are given a 9 x 9 Sudoku board board.
A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"board": [["1","2",".",".","3",".",".",".","."],
                         ["4",".",".","5",".",".",".",".","."],
                         [".","9","8",".",".",".",".",".","3"],
                         ["5",".",".",".","6",".",".",".","4"],
                         [".",".",".","8",".","3",".",".","5"],
                         ["7",".",".",".","2",".",".",".","6"],
                         [".",".",".",".",".",".","2",".","."],
                         [".",".",".","4","1","9",".",".","8"],
                         [".",".",".",".","8",".",".","7","9"]]},
     "output": True},
    {"input": {"board": [["1","2",".",".","3",".",".",".","."],
                         ["4",".",".","5",".",".",".",".","."],
                         [".","9","1",".",".",".",".",".","3"],
                         ["5",".",".",".","6",".",".",".","4"],
                         [".",".",".","8",".","3",".",".","5"],
                         ["7",".",".",".","2",".",".",".","6"],
                         [".",".",".",".",".",".","2",".","."],
                         [".",".",".","4","1","9",".",".","8"],
                         [".",".",".",".","8",".",".","7","9"]]},
     "output": False},
]

COMPLEXITY = """
Complexity
Time: O(81) = O(1) (fixed 9×9 board)
Space: O(1) (at most 27 sets holding up to 9 digits each)
"""


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxs = [set() for _ in range(9)]

    # iterate over row and column (and box)
    for r in range(9):
        for c in range(9):
            b = 3 * (r // 3) + (c // 3)

            # get value
            s = board[r][c]
            if s == '.':
                continue
            v = int(s) - 1  # convert to int and shift range from 1-9 to 0-8

            # check validity
            if (v in rows[r]) or (v in cols[c]) or (v in boxs[b]):
                return False

            # add value
            rows[r].add(v)
            cols[c].add(v)
            boxs[b].add(v)

    return True


function = isValidSudoku


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
