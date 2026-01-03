"""
Binary Tree Maximum Path Sum

def max_path_sum(root: Optional[BinaryTreeNode]) -> int:

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them.
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional, List

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3])}, "result": 6},
    {"inputs": {"root": BinaryTreeNode.from_list([-15,10,20,None,None,15,5,-5])}, "result": 40},
]

COMPLEXITY = """
Complexity
Time: O(n) — each node visited once
Space: O(h) recursion stack
Worst case: O(n)
Balanced tree: O(log n)
"""

def max_path_sum(root: Optional[BinaryTreeNode]) -> int:

    def get_best_and_current(root_: Optional[BinaryTreeNode]) -> tuple[int, int]:
        if root_ is None:
            return 0, 0

        left_best, left_current = get_best_and_current(root_.left)
        right_best, right_current = get_best_and_current(root_.right)

        current = root_.val + max(0, left_current, right_current)
        best = max(
            left_best,
            right_best,
            current,
            max(0, left_current) + max(0, right_current) + root_.val
        )

        return best, current

    return get_best_and_current(root)[0]


function = max_path_sum


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
