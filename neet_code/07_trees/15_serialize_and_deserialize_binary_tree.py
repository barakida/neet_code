"""
Serialize and Deserialize Binary Tree

# Encodes a tree to a single string.
def serialize(root: Optional[BinaryTreeNode]) -> str:


# Decodes your encoded data to tree.
def deserialize(data: list[Optional[int]]) -> Optional[BinaryTreeNode]:


Implement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into a sequence of bits so that
it can be stored or sent across a network to be reconstructed later in another computer environment.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the
original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.
Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree.
You do not necessarily need to follow this format.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional, List

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3,None,None,4,5])}, "result": [1,2,3,None,None,4,5]},
    {"inputs": {"root": BinaryTreeNode.from_list([])}, "result": []},
]

COMPLEXITY = """

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
