from collections import deque
from typing import Optional


class UndirectedGraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        values = []

        queue = deque()
        queue.append(self)
        used = set()
        used.add(self.val)

        while queue:
            node = queue.popleft()
            while len(values) <node.val:
                values.append(list())
            if not values[node.val - 1]:
                for n in node.neighbors:
                    values[node.val - 1].append(n.val)
                    if not n.val in used:
                        queue.appendleft(n)

        return values

    @classmethod
    def from_list(cls, values: list[list[int]]) -> Optional["UndirectedGraphNode"]:

        if not values:
            return None

        node_list = dict()

        def dfs(val) -> UndirectedGraphNode:
            if val not in node_list:
                node_list[val] = UndirectedGraphNode(val)
                for neighbor_val in values[val - 1]:
                    node_list[val].neighbors.append(dfs(neighbor_val))

            return node_list[val]

        return dfs(1)


def main():
    undirected_graph = UndirectedGraphNode.from_list([[2], [1, 3], [2]])
    print(undirected_graph)


if __name__ == '__main__':
    main()
