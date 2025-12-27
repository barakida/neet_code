"""
Merge Two Sorted Linked Lists
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"list1": [1, 2, 4], "list2": [1, 3, 5]}, "output": [1,1,2,3,4,5]},
    {"input": {"list1": [], "list2": [1, 2]}, "output": [1, 2]},
    {"input": {"list1": [], "list2": []}, "output": []},
]

COMPLEXITY = """
Complexity
Time: O(n+m) — each node visited once.
Space: O(1) — no new nodes created (we just rewire existing ones).
"""


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    node = head
    node_1, node_2 = list1, list2

    while node_1 and node_2:
        if node_1.val <= node_2.val:
            node.next = node_1
            node_1 = node_1.next
        else:  # node_1.val > node_2.val
            node.next = node_2
            node_2 = node_2.next
        node = node.next

    node.next = node_1 or node_2

    return head.next


function = mergeTwoLists


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
