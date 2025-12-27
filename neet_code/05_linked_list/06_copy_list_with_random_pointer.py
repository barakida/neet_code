"""
Copy Linked List with Random Pointer
def copyRandomList(head: Optional[Node]) -> Optional[Node]:

You are given the head of a linked list of length n. Unlike a singly linked list,
each node contains an additional pointer random, which may point to any node in the list, or null.
Create a deep copy of the list. The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.
In the examples, the linked list is represented as a list of n nodes.
Each node is represented as a pair of [val, random_index]
where random_index is the index of the node (0-indexed) that the random pointer points to,
or null if it does not point to any node.

Example 1:
Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Example 2:
Input: head = [[1,null],[2,2],[3,2]]
Output: [[1,null],[2,2],[3,2]]

Constraints:
0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.
"""

from typing import Optional


class ListNodeWithRandom:
    def __init__(self, idx: int = None, value: int = None,
                 next_node: "ListNodeWithRandom" = None, random: "ListNodeWithRandom" = None):
        self.idx = idx
        self.val = value
        self.next = next_node
        self.random = random

    def __repr__(self) -> str:
        return str(self._present_all_())

    def _present_self(self):
        return [self.val, self.random.idx if self.random else self.random]

    def _present_all_(self):
        values = list()
        p = self
        while p:
            values.append(p._present_self())
            p = p.next
        return values

    @classmethod
    def from_list(cls, values: list[list[int]]) -> "ListNodeWithRandom":
        root = cls()

        p = root
        nodes_list = list()
        for v, _ in values:
            nodes_list.append(cls(value=v, idx=len(nodes_list)))
            p.next = nodes_list[-1]
            p = p.next

        p = root.next
        for _, r in values:
            if r is not None:
                p.random = nodes_list[r]
            p = p.next

        return root.next


EXAMPLES = [
    {"input": {"head": [[3, None], [7, 3], [4, 0], [5, 1]]}, "output": [[3, None], [7, 3], [4, 0], [5, 1]]},
    {"input": {"head": [[1, None], [2, 2], [3, 2]]}, "output": [[1, None], [2, 2], [3, 2]]},
]

COMPLEXITY = """
Complexity
O(n) time, O(1) space
"""


def copyRandomList(head: Optional[ListNodeWithRandom]) -> Optional[ListNodeWithRandom]:
    # duplicate nodes
    p = head
    while p:
        p.next = ListNodeWithRandom(idx=p.idx, value=p.val, next_node=p.next)
        p = p.next.next

    # set 'random' for new nodes
    p = head
    while p:
        p.next.random = p.random.next if p.random else None
        p = p.next.next

    # split lists
    root = ListNodeWithRandom()
    p1, p2 = head, root
    while p1:
        p2.next = p1.next
        p1.next = p1.next.next
        p1, p2 = p1.next, p2.next

    return root.next


def main():
    for example in EXAMPLES:
        head = ListNodeWithRandom.from_list(example["input"]["head"])
        expected_result = example["output"]
        actual_result = copyRandomList(head=head)
        print(f"expected result: {expected_result}")
        print(f"actual result:   {actual_result}")
        print()


if __name__ == '__main__':
    main()
