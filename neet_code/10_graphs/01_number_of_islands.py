"""
Number of Islands

def num_islands(grid: List[List[str]]) -> int:

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Constraints:
1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"grid": [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]}, "output": 1},
    {"input": {"grid": [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]}, "output": 4},
]

COMPLEXITY = """
Let:
R = number of rows
C = number of columns

Time Complexity
Every cell is visited at most once O(R⋅C)

Space Complexity
DFS recursion stack: O(R · C) worst case (all land)
BFS queue: O(min(R·C))

If modifying the grid is not allowed, you add a visited matrix → still O(R·C) space.
"""


def num_islands(grid: List[List[str]]) -> int:
    counts = 0

    n_rows = len(grid)
    n_cols = len(grid[0])

    def sink_island(r_: int, c_: int) -> None:
        if not 0 <= r_ < n_rows or not 0 <= c_ < n_cols:
            return
        if grid[r_][c_] == "0":
            return

        grid[r_][c_] = "0"
        sink_island(r_-1, c_)
        sink_island(r_+1, c_)
        sink_island(r_, c_-1)
        sink_island(r_, c_+1)

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == '1':
                counts += 1
                sink_island(r, c)

    return counts

function = num_islands


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)