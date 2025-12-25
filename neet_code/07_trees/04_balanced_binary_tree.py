"""
Balanced Binary Tree
def is_balanced(root: BinaryTreeNode) -> bool:

Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which
the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
"""

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,None,None,4])}, "result": True},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,None,None,4,None,5])}, "result": False},
    {"inputs": {"root": BinaryTreeNode.from_list([])}, "result": True},
]

COMPLEXITY = """
Complexity
Time: O(n) (each node visited once)
Space: O(h) recursion stack (height of tree)
"""


def is_balanced(root: BinaryTreeNode) -> bool:

    def get_depth_and_is_balanced(root_: BinaryTreeNode) -> tuple[int, bool]:
        if root_ is None:
            return 0, True

        depth_left, balanced_left = get_depth_and_is_balanced(root_.left)
        if not balanced_left:
            return 1 + depth_left, False

        depth_right, balanced_right = get_depth_and_is_balanced(root_.right)
        if not balanced_right:
            return 1 + depth_right, False

        depth_ = 1 + max(depth_left, depth_right)
        is_balanced_ = -1 <= depth_right - depth_left <= 1

        return depth_, is_balanced_

    return get_depth_and_is_balanced(root)[1]


function = is_balanced


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
