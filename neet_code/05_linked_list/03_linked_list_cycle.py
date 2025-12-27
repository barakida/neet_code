"""
Linked List Cycle Detection
def hasCycle(head: Optional[ListNode]) -> bool:

Given the beginning of a linked list head, return true if there is a cycle in the linked list.
Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists.
The tail node of the list will set it's next pointer to the index-th node.
If index = -1, then the tail node points to null and no cycle exists.
Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode, list_to_linkedlist
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"head": [1, 2, 3, 4], "index": 1}, "output": True},
    {"input": {"head": [1, 2], "index": -1}, "output": False},
]

COMPLEXITY = """
Complexity
Time: O(n) — each pointer visits at most ~2n nodes.
Space: O(1) — only two pointers.
"""


def hasCycle(head: Optional[ListNode]) -> bool:
    node_1 = head
    node_2 = head

    while node_2.next and node_2.next.next:

        node_1 = node_1.next
        node_2 = node_2.next.next
        if node_1 == node_2:
            return True

    return False


function = hasCycle


if __name__ == '__main__':
    for example in EXAMPLES:
        print(example)
        head = list_to_linkedlist(example["input"]["head"])

        if example["input"]["index"] >= 0:
            node_1 = None
            node_last = head
            for idx in range(len(example["input"]["head"]) - 1):
                if example["input"]["index"] == idx:
                    node_1 = node_last
                node_last = node_last.next
            node_last.next = node_1

        print(hasCycle(head=head))
