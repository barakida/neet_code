"""
Binary Tree Level Order Traversal

def level_order(root: Optional[BinaryTreeNode]) -> List[List[int]]:

Given a binary tree root, return the level order traversal of it as a nested list,
where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from queue import Queue
from typing import List, Optional

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5,6,7])}, "result": [[1],[2,3],[4,5,6,7]]},
    {"inputs": {"root": BinaryTreeNode.from_list([1])}, "result": [[1]]},
    {"inputs": {"root": BinaryTreeNode.from_list([])}, "result": []},
]

COMPLEXITY = """
Time Complexity O(n)
Each node is enqueued and dequeued exactly once
Extra queues don’t change the asymptotic time

Space Complexity O(n)
In the worst case, the queue(s) can hold up to O(n) nodes
Plus the output list (which always costs O(n))
"""

from collections import deque
from typing import List, Optional

def level_order(root: Optional[BinaryTreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


"""
GPT Solution
def level_order(root: Optional[BinaryTreeNode]) -> List[List[int]]:
    result = []

    def dfs(node, level):
        if not node:
            return

        if level == len(result):
            result.append([])

        result[level].append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result
"""

function = level_order


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
