"""
Reverse Linked List
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"head": [0, 1, 2, 3]}, "output": [3, 2, 1, 0]},
    {"input": {"head": []}, "output": []},
]

COMPLEXITY = """
Complexity
Time: O(n) — single pass through all nodes.
Space: O(1) — no extra data structures.
"""


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    node_prev = None
    node_curr = head
    while node_curr is not None:
        next_node = node_curr.next
        node_curr.next = node_prev
        node_prev = node_curr
        node_curr = next_node
    return node_prev


function = reverseList


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
