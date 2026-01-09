"""
Number of Connected Components in an Undirected Graph

def count_components(n: int, edges: List[List[int]]) -> int:

There is an undirected graph with n nodes.
There is also an edges array, where edges[i] = [a, b] means that
there is an edge between node a and node b in the graph.
The nodes are numbered from 0 to n - 1.
Return the total number of connected components in that graph.

Example 1:
Input:
n=3
edges=[[0,1], [0,2]]
Output:
1

Example 2:
Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output:
2

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
from typing import List

EXAMPLES = [
    {"input": {"n": 3, "edges": [[0, 1], [0, 2]]}, "output": 1},
    {"input": {"n": 6, "edges": [[0,1], [1,2], [2,3], [4,5]]}, "output": 2},
]

COMPLEXITY = """
let:
V = n (nodes)
E = len(edges)

Union-Find
Time: O(V + E · α(V)) ≈ O(V + E)
Space: O(V)
(α is the inverse Ackermann function, effectively constant.)
"""


def count_components(n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x

    def union(a: int, b: int) -> bool:
        parent_a, parent_b = find(a), find(b)

        # no union needed
        if parent_a == parent_b:
            return False

        # join
        if rank[parent_a] < rank[parent_b]:
            parent[parent_a] = parent_b
        elif rank[parent_a] > rank[parent_b]:
            parent[parent_b] = parent_a
        else:  # rank[parent_a] < rank[parent_b]
            parent[parent_b] = parent_a
            rank[parent_a] += 1

        return True

    for a, b in edges:
        union(a, b)

    return len({find(x) for x in range(n)})


function = count_components


def main():
    for e in EXAMPLES:
        print(f"Input: {e['input']}")
        print(f"expected: {e['output']}")
        print(f"Output: {function(**e['input'])}")
        print("\n\n")

    print(COMPLEXITY)


if __name__ == "__main__":
    main()
