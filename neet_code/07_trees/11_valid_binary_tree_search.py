"""
Valid Binary Search Tree

def is_valid_bst(root: Optional[TreeNode]) -> bool:

Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
A valid binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import Optional, List

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([2,1,3])}, "result": True},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3])}, "result": False},
]

COMPLEXITY = """
COMPLEXITY
Time: O(n) — each node visited once
Space: O(h) recursion stack
worst case: O(n)
balanced tree: O(log n)
"""

def is_valid_bst(root: Optional[BinaryTreeNode]) -> bool:
    def _get_valid_min_max(root_: Optional[BinaryTreeNode]) -> tuple[bool, Optional[int], Optional[int]]:
        if root_ is None:
            return True, None, None

        left_valid, left_min, left_max = _get_valid_min_max(root_.left)
        right_valid, right_min, right_max = _get_valid_min_max(root_.right)

        is_valid = left_valid and right_valid and (left_max is None or left_max < root_.val) and (right_min is None or right_min > root_.val)

        return is_valid, root_.val if left_min is None else left_min, root_.val if right_max is None else right_max

    return _get_valid_min_max(root)[0]


function = is_valid_bst


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()


"""
GPT Solution

def is_valid_bst(root: Optional[BinaryTreeNode]) -> bool:
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (
            dfs(node.left, low, node.val) and
            dfs(node.right, node.val, high)
        )

    return dfs(root, float("-inf"), float("inf"))
"""