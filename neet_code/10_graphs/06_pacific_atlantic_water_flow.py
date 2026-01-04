"""
Pacific Atlantic Water Flow

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:

You are given a rectangular island heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).
The islands borders the Pacific Ocean from the top and left sides,
and borders the Atlantic Ocean from the bottom and right sides.
Water can flow in four directions (up, down, left, or right)
from a cell to a neighboring cell with height equal or lower.
Water can also flow into the ocean from cells adjacent to the ocean.
Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans.
Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell.
You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[0,1]]

Constraints:
1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""

EXAMPLES = [
    {"input": {"heights": [
        [4,2,7,3,4],
        [7,4,6,4,7],
        [6,3,5,3,6]
    ]}, "output": [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]},
    {"input": {"heights": [[1],[1]]}, "output": [[0,0],[0,1]]},
]

COMPLEXITY = """
Complexity Summary Table
Aspect	            Complexity
Time	            O(R · C)
Visited Sets	    O(R · C)
Recursion Stack	    O(R · C)
Output	            O(R · C)
"""

from collections import deque
from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])
    sea_sets = {"pacific": set(), "atlantic": set()}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r_: int, c_: int, sea: str) -> None:
        sea_sets[sea].add((r_, c_))
        for (dr, dc) in directions:
            r_next, c_next = r_ + dr, c_ + dc
            if (0 <= r_next < rows and 0 <= c_next < cols and
                    not (r_next, c_next) in sea_sets[sea] and
                    heights[r_next][c_next] >= heights[r_][c_]):
                dfs(r_next, c_next, sea)

    # pacific
    for r in range(rows):
        dfs(r, 0, "pacific")
    for c in range(cols):
        dfs(0, c, "pacific")

    # atlantic
    for r in range(rows):
        dfs(r, cols - 1, "atlantic")
    for c in range(cols):
        dfs(rows - 1, c, "atlantic")

    return [[r, c] for (r, c) in sea_sets["pacific"] & sea_sets["atlantic"]]


function = pacific_atlantic


if __name__ == '__main__':
    import numpy as np

    for e in EXAMPLES:
        print(f"{np.array(e['input']["heights"])}")
        print(function(**e['input']))
        print("\n\n")

    print("\nComplexity:", COMPLEXITY)


"""

"""