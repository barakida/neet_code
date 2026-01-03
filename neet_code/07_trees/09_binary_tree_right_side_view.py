"""
Binary Tree Right Side View

def right_side_view(root: Optional[TreeNode]) -> List[int]:

You are given the root of a binary tree.
Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:
Input: root = [1,2,3]
Output: [1,3]

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,7]

Constraints:
0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""
from typing import Optional, List

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3])}, "result": [1,3]},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5,6,7])}, "result": [1,3,7]},
]

COMPLEXITY = """
Complexity
Time: O(n) — each node visited once
Space: O(h) recursion stack
    Worst case (skewed tree): O(n)
    Balanced tree: O(log n)
Output list: O(n) in worst case
"""

def right_side_view(root: Optional[BinaryTreeNode]) -> List[int]:
    results = []

    def _right_side_view(root_: Optional[BinaryTreeNode], level: int) -> None:

        if root_ is None:
            return

        if level > len(results):
            results.append(root_.val)

        _right_side_view(root_=root_.right, level=level+1)
        _right_side_view(root_=root_.left, level=level+1)

    _right_side_view(root, 1)

    return results


function = right_side_view


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()

"""
important to remember

from collections import deque
queue = deque([root])
node = queue.popleft()
result.append(node.val)
"""

