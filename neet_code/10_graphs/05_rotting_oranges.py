"""
Rotting Fruit

def oranges_rotting(grid: List[List[int]]) -> int:

You are given a 2-D matrix grid. Each cell can have one of three possible values:
0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit,
then the fresh fruit also becomes rotten.
Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining.
If this state is impossible within the grid, return -1.

Example 1:
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
Output: 4

Example 2:
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
Output: -1

Constraints:
1 <= grid.length, grid[i].length <= 10
"""

EXAMPLES = [
    {"input": {"grid": [[1,1,0],[0,1,1],[0,1,2]]}, "output": 4},
    {"input": {"grid": [[1,0,1],[0,2,0],[1,0,1]]}, "output": -1},
]

COMPLEXITY = """
Final Complexity Summary
Aspect	            Complexity
Time	            O(R · C)
Aux Space (queue)	O(R · C)
Extra Memory	    O(1) (in-place)
"""

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    queue = deque()
    rows, cols = len(grid), len(grid[0])
    targets = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
                targets += 1
            elif grid[r][c] == 1:
                targets += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:

            r, c, time = queue.popleft()
            targets -= 1

            for (d_r, d_c) in directions:
                r_next, c_next = r + d_r, c + d_c
                if 0 <= r_next < rows and 0 <= c_next < cols and grid[r_next][c_next] == 1:
                    grid[r_next][c_next] = 2
                    queue.append((r_next, c_next, time + 1))

    return -1 if targets else time



function = oranges_rotting


if __name__ == '__main__':
    import numpy as np
    for e in EXAMPLES:
        print(f"{np.array(e['input']["grid"])}")
        print(function(**e['input']))
        print("\n\n")

    print("\nComplexity:", COMPLEXITY)
