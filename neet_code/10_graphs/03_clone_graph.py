"""
Clone Graph

def clone_graph(node: Optional[UndirectedGraphNode]) -> Optional[UndirectedGraphNode]:

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list.
An adjacency list is a mapping of nodes to lists, used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph.
The index of each node within the adjacency list is the same as the node's value (1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation:
    There are 3 nodes in the graph.
    Node 1: val = 1 and neighbors = [2].
    Node 2: val = 2 and neighbors = [1, 3].
    Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: The graph is empty.

Constraints:
0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
"""

from typing import List, Optional

from neet_code.classes.undirected_graph_node import UndirectedGraphNode

EXAMPLES = [
    {"input": {"node": UndirectedGraphNode.from_list([[2],[1,3],[2]])}, "output": [[2],[1,3],[2]]},
    {"input": {"node": UndirectedGraphNode.from_list([[]])}, "output": [[]]},
    {"input": {"node": UndirectedGraphNode.from_list([])}, "output": []},
]

COMPLEXITY = """
Final Complexity Summary
Aspect	        Complexity
Time	        O(V + E)
Aux Space	    O(V)
Output Space	O(V + E)
"""


def clone_graph(node: Optional[UndirectedGraphNode]) -> Optional[UndirectedGraphNode]:
    if node is None:
        return []

    clone_dict = dict()

    def dfs_cloning(node_: Optional[UndirectedGraphNode]) -> Optional[UndirectedGraphNode]:

        if node_.val not in clone_dict:
            clone_dict[node_.val] = UndirectedGraphNode(node_.val)
            for n in node_.neighbors:
                clone_dict[node_.val].neighbors.append(dfs_cloning(n))

        return clone_dict[node_.val]

    return dfs_cloning(node)


function = clone_graph


if __name__ == '__main__':
    for e in EXAMPLES:
        print(f"input: {e['input']}  |  expected_output: {e['output']}  |  output: {function(**e['input'])}")

    print("\nComplexity:", COMPLEXITY)
