"""
Subtree of Another Tree
def is_subtree(root: Optional[BinaryTreeNode], subRoot: Optional[BinaryTreeNode]) -> bool:

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
"""
from typing import Optional

from neet_code.utils.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5]), "subRoot": BinaryTreeNode.from_list([2,4,5])}, "result": True},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5,None,None,6]), "subRoot": BinaryTreeNode.from_list([2,4,5])}, "result": False},
]

COMPLEXITY = """
COMPLEXITY:
Let:
n = number of nodes in root
m = number of nodes in subRoot

Worst case:
you call is_same_tree at many nodes → O(n * m)
With n, m <= 100, this is totally acceptable.

Space:
recursion stack O(h) for subtree traversal (height)
"""

def is_same_tree(root_1: Optional[BinaryTreeNode], root_2: Optional[BinaryTreeNode]) -> bool:
    if not root_1 and not root_2:
        return True
    elif not root_1 or not root_2:
        return False
    elif root_1.val != root_2.val:
        return False
    return is_same_tree(root_1.left, root_2.left) and is_same_tree(root_1.right, root_2.right)


def is_subtree(root: Optional[BinaryTreeNode], subRoot: Optional[BinaryTreeNode]) -> bool:

    # check current node
    if is_same_tree(root, subRoot):
        return True

    # check left and right (while dealing with "None")
    subtree_in_left = is_subtree(root.left, subRoot) if root.left is not None else False
    subtree_in_right = is_subtree(root.right, subRoot) if root.right is not None else False

    return subtree_in_left or subtree_in_right


function = is_subtree


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
