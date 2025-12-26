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

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3])}, "result": [1,3]},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5,6,7])}, "result": [1,3,7]},
]

COMPLEXITY = """

"""

def right_side_view(root: Optional[BinaryTreeNode]) -> List[int]:
    pass


function = right_side_view


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
