"""
Maximum Depth of Binary Tree

def get_max_depth(root: BinaryTreeNode) -> int:

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the
longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""

from neet_code.utils.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,None,None,4])}, "result": 3},
    {"inputs": {"root": BinaryTreeNode.from_list([])}, "result": 0},
]


def get_max_depth(root: BinaryTreeNode) -> int:
    if root is None or root.val is None:
        return 0
    return 1 + max(get_max_depth(root.left), get_max_depth(root.right))


function = get_max_depth


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]


if __name__ == '__main__':
    main()