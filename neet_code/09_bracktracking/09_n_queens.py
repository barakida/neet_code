"""
N-Queens

def solve_n_queens(n: int) -> List[List[str]]:

The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.
A queen in a chessboard can attack horizontally, vertically, and diagonally.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a unique board layout where the queen pieces are placed.
'Q' indicates a queen and '.' indicates an empty space.
You may return the answer in any order.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 8
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"n": 4}, "output": [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]},
    {"input": {"n": 1}, "output": [["Q"]]},
]

COMPLEXITY = """
Let:
n = board size
S = number of valid solutions (output size)

Final Big-O Summary
Category	                Complexity
Time	                    O(n! + S·n²)
Space (aux)	                O(n²)
Space (including output)	O(S·n²)
"""


from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    solutions: List[List[str]] = []
    cols = set()      # used columns: c
    diag1 = set()     # used main diagonals: r - c
    diag2 = set()     # used anti diagonals: r + c

    board = [["."] * n for _ in range(n)]

    def dfs(r: int) -> None:
        if r == n:
            solutions.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            # place
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board[r][c] = "Q"

            dfs(r + 1)

            # unplace
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    dfs(0)
    return solutions


function = solve_n_queens


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
