"""
Diameter of Binary Tree


The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree.
The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Note that the path can not include the same node twice.
Given the root of a binary tree root, return the diameter of the tree.

Example 1:
Input: root = [1,null,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:
Input: root = [1,2,3]
Output: 2

Constraints:
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

"""

from neet_code.classes.binary_tree_node import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([1,None,2,3,4,5])}, "result": 3},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,3])}, "result": 2},
]

COMPLEXITY = """
Complexity
Time: O(n) (each node visited once)
Space: O(h) recursion stack (height of tree)
"""


def get_diameter(root: BinaryTreeNode) -> int:

    def get_diameter_and_depth(root_: BinaryTreeNode) -> tuple[int, int]:
        if root_ is None:
            return 0, 0

        diameter_left, depth_left = get_diameter_and_depth(root_.left)
        diameter_right, depth_right = get_diameter_and_depth(root_.right)

        diameter_ = max(diameter_left, diameter_right, depth_left + depth_right)
        depth_ = max(depth_left, depth_right) + 1

        return diameter_, depth_

    diameter, depth = get_diameter_and_depth(root)

    return diameter


function = get_diameter


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()


"""
      1
null     2
      3     4
   5    
"""