import random
from queue import Queue
from typing import Callable


class BinaryTreeNode:
    def __init__(self, val: float, left: "BinaryTreeNode" = None, right: "BinaryTreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.to_list())

    @classmethod
    def from_list(cls, values: list[float]) -> "BinaryTreeNode":
        queue = Queue()

        if not values:
            return BinaryTreeNode(None)

        head = BinaryTreeNode(values[0])
        queue.put(head)
        for idx in range(1, len(values), 2):
            node = queue.get()
            node.left = BinaryTreeNode(values[idx])
            queue.put(node.left)
            if idx + 1 < len(values):
                node.right = BinaryTreeNode(values[idx + 1])
                queue.put(node.right)
        queue.empty()

        return head

    def to_list(self):

        # init queue
        queue = Queue()
        queue.put(self)

        # iterate over tree
        result = list()
        while not queue.empty():
            node = queue.get()
            result.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        if len(result) == 1 and result[0] is None:
            return []

        return result


def test_binary_tree_function(function: Callable, example: dict) -> None:
    result = function(**example["inputs"])
    result = result.to_list() if isinstance(result, BinaryTreeNode) else result
    print(f"inputs: {example['inputs']}  |  result: {result}  |  true: {example["result"]}")

