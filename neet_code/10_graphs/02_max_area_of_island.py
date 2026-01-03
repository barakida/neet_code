"""
Max Area of Island

def max_area_of_island(grid: List[List[int]]) -> int:

You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:
1 <= grid.length, grid[i].length <= 50
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"grid": [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]]}, "output": 6},
]

COMPLEXITY = """
Final Complexity Summary
Aspect	                    Complexity
Time	                    O(R · C)
Aux Space (DFS stack)	    O(R · C)
Extra Memory	            O(1) (in-place)
"""


def max_area_of_island(grid: List[List[int]]) -> int:
    max_area = 0
    current_area = 0

    n_rows, n_cols = len(grid), len(grid[0])

    def sink_island(r_: int, c_: int) -> None:
        nonlocal current_area

        if not 0 <= r_ < n_rows or not 0 <= c_ < n_cols:
            return
        if grid[r_][c_] == 0:
            return

        current_area += 1
        grid[r_][c_] = 0
        sink_island(r_ + 1, c_)
        sink_island(r_ - 1, c_)
        sink_island(r_, c_ + 1)
        sink_island(r_, c_ - 1)

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == 1:
                current_area = 0
                sink_island(r, c)
                max_area = max(max_area, current_area)

    return max_area


function = max_area_of_island


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
