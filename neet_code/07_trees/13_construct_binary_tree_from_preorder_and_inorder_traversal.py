"""
Construct Binary Tree from Preorder and Inorder Traversal

def build_tree(preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:

You are given two integer arrays preorder and inorder.
preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""
from typing import Optional, List

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"preorder": [1,2,3,4], "inorder": [2,1,3,4]}, "result": BinaryTreeNode.from_list([1,2,3,None,None,None,4])},
    {"inputs": {"preorder": [1], "inorder": [1]}, "result": BinaryTreeNode.from_list([1])},
]

COMPLEXITY = """
"""


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
    if not preorder or not inorder:
        return None

    inorder_value_to_idx = {v: i for i, v, in enumerate(inorder)}
    idx = 0

    def helper(left: int, right: int) -> Optional[BinaryTreeNode]:
        nonlocal idx

        if left >= right:
            return None

        # build tree node
        root_val = preorder[idx]
        root = BinaryTreeNode(root_val)
        idx += 1

        # add node left and right
        right_, left_ = inorder_value_to_idx[root_val], inorder_value_to_idx[root_val] + 1
        root.left = helper(left, right_)
        root.right = helper(left_, right)

        return root

    return helper(0, len(inorder))

function = build_tree


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
