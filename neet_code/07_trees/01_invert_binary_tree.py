"""
Invert Binary Tree
def invert_binary_tree(root: BinaryTreeNode) -> BinaryTreeNode:

You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function


EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,4,5,6,7])}, "result": [1,3,2,7,6,5,4]},
    {"inputs": {"root": BinaryTreeNode.from_list([3,2,1])}, "result": [3,1,2]},
    {"inputs": {"root": BinaryTreeNode.from_list([])}, "result": []},
]


# from queue import Queue
# def invert_binary_tree(root: BinaryTreeNode) -> BinaryTreeNode:
#     queue = Queue()
#     queue.put(root)
#     while not queue.empty():
#         node = queue.get()
#         if node is None:
#             continue
#         node.left, node.right = node.right, node.left
#         queue.put(node.left)
#         queue.put(node.right)
#
#     return root


def invert_binary_tree(root: BinaryTreeNode) -> BinaryTreeNode:
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    if root.left:
        invert_binary_tree(root.left)
    if root.right:
        invert_binary_tree(root.right)

    return root


function = invert_binary_tree


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]


if __name__ == '__main__':
    main()
