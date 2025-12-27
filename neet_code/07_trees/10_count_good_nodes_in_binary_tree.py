"""
Count Good Nodes in Binary Tree

def good_nodes(root: BinaryTreeNode) -> int:

Within a binary tree, a node x is considered good if the path from the
root of the tree to the node x contains no nodes with a value greater than the value of node x
Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:
Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:
Input: root = [1,2,-1,3,4]
Output: 4

Constraints:
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""

from typing import Optional, List

from neet_code.classes.binary_tree import BinaryTreeNode, test_binary_tree_function

EXAMPLES = [
    {"inputs": {"root": BinaryTreeNode.from_list([2,1,1,3,None,1,5])}, "result": 3},
    {"inputs": {"root": BinaryTreeNode.from_list([1,2,-1,3,4])}, "result": 4},
]

COMPLEXITY = """
Time: O(n) — each node visited once
Space: O(h) recursion stack
worst case: O(n)
balanced tree: O(log n)
"""

def good_nodes(root: BinaryTreeNode) -> int:
    count = 0

    def traverse(root_: BinaryTreeNode, current_max: int):
        nonlocal count

        if not root_:
            return
        if current_max <= root_.val:
            count += 1

        current_max = max(current_max, root_.val)
        traverse(root_.left, current_max)
        traverse(root_.right, current_max)

    traverse(root, root.val)

    return count


function = good_nodes


def main():
    [test_binary_tree_function(function=function, example=example) for example in EXAMPLES]
    print(COMPLEXITY)


if __name__ == '__main__':
    main()

"""
important to remember

from collections import deque
queue = deque([root])
node = queue.popleft()
result.append(node.val)
"""

"""
GPT ulternative

def good_nodes(root: BinaryTreeNode) -> int:
    def dfs(node, current_max):
        if not node:
            return 0
        good = 1 if node.val >= current_max else 0
        current_max = max(current_max, node.val)
        return good + dfs(node.left, current_max) + dfs(node.right, current_max)

    return dfs(root, root.val)
"""

"""
GPT loop alternative

def good_nodes(root: BinaryTreeNode) -> int:
    count = 0
    stack = [(root, root.val)]

    while stack:
        node, current_max = stack.pop()
        if node.val >= current_max:
            count += 1
        new_max = max(current_max, node.val)
        if node.left:
            stack.append((node.left, new_max))
        if node.right:
            stack.append((node.right, new_max))

    return count
"""

