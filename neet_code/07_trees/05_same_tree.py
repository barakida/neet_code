"""
Same Binary Tree
def is_same_tree(p: BinaryTreeNode, q: BinaryTreeNode) -> bool:

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"p": BinaryTreeNode.from_list([1,2,3]), "q": BinaryTreeNode.from_list([1,2,3])}, "result": True},
    {"inputs": {"p": BinaryTreeNode.from_list([4,7]), "q": BinaryTreeNode.from_list([4,None,7])}, "result": False},
    {"inputs": {"p": BinaryTreeNode.from_list([1,2,3]), "q": BinaryTreeNode.from_list([1,3,2])}, "result": False},
]

COMPLEXITY = """
Complexity
Time: O(n) (each node visited once)
Space: O(h) recursion stack (height of tree)
"""


def is_same_tree(p: BinaryTreeNode, q: BinaryTreeNode) -> bool:

    # dealing with "None"
    if p is None and q is None:
        return True
    elif p is None and q is not None:
        return False
    elif p is not None and q is None:
        return False

    # dealing with value
    if p.val != q.val:
        return False

    # dealing with children
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


function = is_same_tree


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
