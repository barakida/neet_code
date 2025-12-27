"""
Kth Smallest Integer in BST

def kth_smallest(root: Optional[BinaryTreeNode], k: int) -> int:

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
"""

from typing import Optional, List

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([2,1,3]), "k": 1}, "result": 1},
    {"inputs": {"root": BinaryTreeNode.from_list([4,3,5,2,None]), "k": 4}, "result": 5},
]

COMPLEXITY = """
COMPLEXITY

"""

def kth_smallest(root: Optional[BinaryTreeNode], k: int) -> int:
    count = 0
    result = None

    def _kth_smallest(root_: Optional[BinaryTreeNode]):
        nonlocal count
        nonlocal result

        if root_ is None or count == k:
            return

        _kth_smallest(root_.left)

        if count < k:
            count += 1
            result = root_.val

        _kth_smallest(root_.right)

    _kth_smallest(root)

    return result


function = kth_smallest


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
