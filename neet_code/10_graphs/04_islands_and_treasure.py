"""
Islands and Treasure

def islands_and_treasure(grid: List[List[int]]) -> None:

You are given a m×n 2D grid initialized with these three possible values:
-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.
Assume the grid can only be traversed up, down, left, or right.
Modify the grid in-place.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""

from typing import List, Optional

from neet_code.classes.undirected_graph_node import UndirectedGraphNode

EXAMPLES = [
    {
        "input": {"grid": [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]
    },
        "output": [
            [3,-1,0,1],
            [2,2,1,-1],
            [1,-1,2,-1],
            [0,-1,3,4]
        ]
    },
    {
        "input": {"grid": [
            [0, -1],
            [2147483647, 2147483647]
        ]
        },
        "output": [
            [0, -1],
            [1, 2]
        ]
    },
]

COMPLEXITY = """
Final Complexity Summary
Aspect	            Complexity
Time	            O(R · C)
Aux Space (queue)	O(R · C)
Extra Memory	    O(1) (in-place)
"""

from collections import deque

def islands_and_treasure(grid: List[List[int]]) -> None:
    queue = deque()
    rows, cols = len(grid), len(grid[0])

    def update_grid(r_: int, c_: int, val: int) -> None:
        if grid[r_][c_] == -1:
            return
        if val and grid[r_][c_] < val:
            return

        grid[r_][c_] = val
        if r_ + 1 < rows:
            queue.append((r_ + 1, c_, val + 1))
        if 0 <= r_ - 1:
            queue.append((r_ - 1, c_, val + 1))
        if c_ + 1 < cols:
            queue.append((r_, c_ + 1, val + 1))
        if 0 <= c_ -1:
            queue.append((r_, c_ - 1, val + 1))

    # find treasures
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                queue.append((r, c, 0))

    # update grid
    while queue:
        (r, c, val) = queue.popleft()
        update_grid(r, c, val)


function = islands_and_treasure


if __name__ == '__main__':
    import numpy as np
    for e in EXAMPLES:
        print(f"{np.array(e['input']["grid"])}\n\n")
        function(**e['input'])
        print(f"{np.array(e['input']["grid"])}\n\n\n")

    print("\nComplexity:", COMPLEXITY)
